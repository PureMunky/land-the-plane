#!/usr/bin/env python3
"""Render an episode script into a single WAV file using Piper TTS.

Usage:
    python scripts/generate.py episodes/001-intent-layer/script.md

Outputs:
    episodes/<slug>/segments/NNNN.wav   per-paragraph chunks
    episodes/<slug>/episode.wav          final concatenated episode

The script is parsed as Markdown. Headings, metadata lines, and the YAML-
ish `**Key:** value` block at the top are skipped. Paragraphs become
chunks. A horizontal rule (`---`) inserts a longer silence break between
sections.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import wave
from pathlib import Path

VOICE_MODEL = Path(__file__).parent.parent / "voices" / "en-us-ryan-medium.onnx"
LENGTH_SCALE = 1.10          # slows phonemes slightly for podcast pacing
SENTENCE_SILENCE = 0.45      # seconds between sentences within a paragraph
PARAGRAPH_SILENCE = 0.65     # seconds between paragraphs within a section
SECTION_SILENCE = 1.40       # seconds at section breaks (---)


META_LINE = re.compile(r"^\*\*([A-Za-z][^*]{0,40}):\*\*\s*(.*)$")
TITLE_LINE = re.compile(r"^#\s+Episode\s+(\d+)\s*[—-]\s*(.+)$")


def parse_metadata(path: Path) -> dict:
    """Extract title, episode number, subtitle, published date, and summary
    from the script's top-of-file metadata block."""
    meta: dict = {"slug": path.parent.name}
    summary_parts: list[str] = []
    in_summary = False

    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped:
            in_summary = False
            continue
        if stripped.startswith("##") or stripped == "---":
            break
        m = TITLE_LINE.match(stripped)
        if m:
            meta["number"] = int(m.group(1))
            meta["title"] = m.group(2).strip()
            continue
        m = META_LINE.match(stripped)
        if m:
            key = m.group(1).strip().lower()
            value = m.group(2).strip()
            if key == "subtitle":
                meta["subtitle"] = value
            elif key == "published":
                meta["published"] = value
            elif key == "summary":
                in_summary = True
                summary_parts = [value] if value else []
            else:
                in_summary = False
            continue
        if in_summary:
            summary_parts.append(stripped)

    if summary_parts:
        meta["summary"] = " ".join(summary_parts).strip()
    return meta


def parse_script(path: Path) -> list[dict]:
    """Return a list of chunks: {'kind': 'speech'|'break', 'text'?: str}."""
    raw = path.read_text(encoding="utf-8")

    chunks: list[dict] = []
    paragraph: list[str] = []
    # Everything before the first `---` is metadata (title heading and the
    # **Key:** value block, including wrapped continuation lines). The
    # parser skips this block entirely; parse_metadata() pulls the fields
    # out separately for the build.
    in_body = False

    def flush():
        if paragraph:
            text = " ".join(paragraph).strip()
            text = clean_for_tts(text)
            if text:
                chunks.append({"kind": "speech", "text": text})
            paragraph.clear()

    for line in raw.splitlines():
        stripped = line.strip()

        if not in_body:
            if stripped == "---":
                in_body = True
            continue

        if not stripped:
            flush()
            continue

        if stripped.startswith("#"):
            flush()
            continue

        if stripped == "---":
            flush()
            chunks.append({"kind": "break"})
            continue

        # Plain paragraph content
        paragraph.append(stripped)

    flush()
    return chunks


def clean_for_tts(text: str) -> str:
    """Strip markdown emphasis and normalise punctuation for the synthesiser."""
    # Remove bold/italic markers but keep the inner text
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    # Smart quotes / em-dashes for cleaner Piper prosody
    text = text.replace("—", " — ").replace("–", " - ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def synth_paragraph(text: str, out_path: Path) -> None:
    """Run Piper on a single paragraph, writing to out_path."""
    cmd = [
        "piper",
        "-m", str(VOICE_MODEL),
        "--length-scale", str(LENGTH_SCALE),
        "--sentence-silence", str(SENTENCE_SILENCE),
        "-f", str(out_path),
    ]
    proc = subprocess.run(
        cmd,
        input=text,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"piper failed (exit {proc.returncode})\n"
            f"stderr: {proc.stderr.strip()}\n"
            f"input:  {text[:120]}..."
        )


def silence_wav(out_path: Path, duration_s: float, sample_rate: int = 22050) -> None:
    """Write a silent mono 16-bit WAV of the given duration."""
    n_frames = int(duration_s * sample_rate)
    with wave.open(str(out_path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)  # 16-bit
        w.setframerate(sample_rate)
        w.writeframes(b"\x00\x00" * n_frames)


def concat_wavs(inputs: list[Path], out_path: Path) -> None:
    """Concatenate mono PCM WAVs by reading their frames and writing one
    output. Doing this through Python's wave module rather than
    `ffmpeg -f concat -c copy` avoids embedding each input's RIFF/WAVE
    header into the output stream — those header bytes were getting
    decoded as audio samples and producing static at paragraph boundaries
    in earlier renders."""
    if not inputs:
        raise ValueError("no input wavs to concat")

    with wave.open(str(inputs[0]), "rb") as first:
        sample_rate = first.getframerate()
        nchannels = first.getnchannels()
        sampwidth = first.getsampwidth()

    with wave.open(str(out_path), "wb") as out:
        out.setnchannels(nchannels)
        out.setsampwidth(sampwidth)
        out.setframerate(sample_rate)
        for p in inputs:
            with wave.open(str(p), "rb") as w:
                if (w.getframerate() != sample_rate
                        or w.getnchannels() != nchannels
                        or w.getsampwidth() != sampwidth):
                    raise RuntimeError(
                        f"WAV format mismatch in {p}: "
                        f"{w.getframerate()}Hz/{w.getnchannels()}ch/"
                        f"{w.getsampwidth() * 8}bit (expected "
                        f"{sample_rate}Hz/{nchannels}ch/{sampwidth * 8}bit). "
                        f"Delete segments/ and re-render to reset."
                    )
                out.writeframes(w.readframes(w.getnframes()))


def wav_duration(path: Path) -> float:
    with wave.open(str(path), "rb") as w:
        return w.getnframes() / float(w.getframerate())


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("script", type=Path, help="path to script.md")
    ap.add_argument("--clean", action="store_true",
                    help="delete existing segments/ before generating")
    ap.add_argument("--preview", type=int, metavar="N", default=None,
                    help="render only the first N speech chunks, write to "
                         "preview.wav (no MP3, no metadata). Useful for "
                         "iterating on the opening or testing voice "
                         "settings without paying the full ~10 min cost.")
    args = ap.parse_args()

    if not VOICE_MODEL.exists():
        print(f"Voice model not found: {VOICE_MODEL}", file=sys.stderr)
        print("Run scripts/install_voice.sh first.", file=sys.stderr)
        return 1

    if not shutil.which("piper"):
        print("piper is not on PATH. Install with: pip install piper-tts",
              file=sys.stderr)
        return 1
    if not shutil.which("ffmpeg"):
        print("ffmpeg is not on PATH. Install with: apt install ffmpeg",
              file=sys.stderr)
        return 1

    episode_dir = args.script.parent
    segments_dir = episode_dir / "segments"
    if args.clean and segments_dir.exists():
        shutil.rmtree(segments_dir)
    segments_dir.mkdir(parents=True, exist_ok=True)

    chunks = parse_script(args.script)
    if args.preview is not None:
        chunks = limit_to_first_n_speech(chunks, args.preview)
        print(f"Preview mode: rendering first {args.preview} speech chunks.")
    word_count = sum(len(c["text"].split()) for c in chunks if c["kind"] == "speech")
    print(f"Parsed {len(chunks)} chunks; ~{word_count} spoken words.")

    paragraph_silence = segments_dir / "_para_silence.wav"
    section_silence = segments_dir / "_section_silence.wav"
    silence_wav(paragraph_silence, PARAGRAPH_SILENCE)
    silence_wav(section_silence, SECTION_SILENCE)

    timeline: list[Path] = []
    speech_idx = 0
    for i, chunk in enumerate(chunks):
        if chunk["kind"] == "break":
            timeline.append(section_silence)
            continue

        seg_path = segments_dir / f"{speech_idx:04d}.wav"
        if seg_path.exists() and seg_path.stat().st_size > 44:
            print(f"  [{speech_idx:04d}] cached: {chunk['text'][:60]}...")
        else:
            print(f"  [{speech_idx:04d}] synth ({len(chunk['text'].split())} "
                  f"words): {chunk['text'][:60]}...")
            synth_paragraph(chunk["text"], seg_path)
        timeline.append(seg_path)

        # Add a short pause unless the next chunk is a section break
        next_is_break = (
            i + 1 < len(chunks) and chunks[i + 1]["kind"] == "break"
        )
        is_last = (i + 1 == len(chunks))
        if not next_is_break and not is_last:
            timeline.append(paragraph_silence)
        speech_idx += 1

    wav_name = "preview.wav" if args.preview is not None else "episode.wav"
    wav_path = episode_dir / wav_name
    print(f"Concatenating {len(timeline)} segments into {wav_path}")
    concat_wavs(timeline, wav_path)

    duration = wav_duration(wav_path)
    minutes = int(duration // 60)
    seconds = int(duration % 60)
    print(f"WAV duration: {minutes}m {seconds}s "
          f"({wav_path.stat().st_size / 1024 / 1024:.1f} MB)")

    if args.preview is not None:
        print(f"Preview ready: {wav_path}")
        return 0

    mp3_path = episode_dir / "episode.mp3"
    print(f"Encoding MP3: {mp3_path}")
    encode_mp3(wav_path, mp3_path)

    meta = parse_metadata(args.script)
    meta.update({
        "duration_seconds": int(round(duration)),
        "duration_hms": f"{minutes:02d}:{seconds:02d}",
        "mp3_filename": mp3_path.name,
        "mp3_size_bytes": mp3_path.stat().st_size,
        "word_count": word_count,
    })
    json_path = episode_dir / "episode.json"
    json_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote metadata: {json_path}")
    print(f"Done. {mp3_path.stat().st_size / 1024 / 1024:.1f} MB MP3.")
    return 0


def limit_to_first_n_speech(chunks: list[dict], n: int) -> list[dict]:
    """Trim the chunk list to the first n speech chunks, preserving any
    section breaks that fall between them."""
    out: list[dict] = []
    speech_count = 0
    for c in chunks:
        if c["kind"] == "speech":
            if speech_count >= n:
                break
            speech_count += 1
        out.append(c)
    return out


def encode_mp3(wav: Path, mp3: Path, bitrate: str = "96k") -> None:
    """Encode WAV to mono MP3 at the given bitrate. 96k mono is a good
    podcast tradeoff: speech-clear, ~12 MB per 30 minutes."""
    cmd = [
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-i", str(wav),
        "-codec:a", "libmp3lame",
        "-b:a", bitrate,
        "-ac", "1",
        str(mp3),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(
            f"ffmpeg mp3 encode failed: {proc.stderr.strip()}"
        )


if __name__ == "__main__":
    raise SystemExit(main())
