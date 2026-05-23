---
description: Render an episode script to MP3
argument-hint: <episode-slug>
---

Render `episodes/$ARGUMENTS/script.md` to MP3 using the local Piper
pipeline.

Steps:

1. Verify `episodes/$ARGUMENTS/script.md` exists. If not, list the
   episodes directory and stop.

2. Verify the voice model is installed by checking for
   `voices/en-us-ryan-medium.onnx`. If missing, run
   `bash scripts/install_voice.sh` first.

3. Run `python3 scripts/generate.py episodes/$ARGUMENTS/script.md`.
   This takes ~10 minutes wall-clock for a 30-minute episode (~3x
   real-time). Run it in the foreground so you can report the final
   duration. Do NOT run it in the background — the user is explicitly
   waiting on the render.

4. When it finishes, report:
   - Duration (`MM:SS`)
   - MP3 size in MB
   - Whether the duration is in the target 25-35 minute band
   - Suggested next step: `/publish $ARGUMENTS`

If `generate.py` fails partway through (e.g. piper crashes on a
chunk), look at the failing paragraph in the script — usually it's a
weird character or an over-long sentence — and ask the user how to
adjust. Do not silently delete or rewrite the script.
