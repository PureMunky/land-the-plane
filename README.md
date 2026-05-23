# Land the Plane

> ⚠️ **Experimental project.** Land the Plane is an in-progress
> experiment in producing a weekly podcast end-to-end through an AI
> pipeline — research, drafting, audio synthesis, and publishing all
> run through Claude Code and Piper TTS. The voice is synthetic.
> Treat any episode as a working draft of an argument, not as
> authoritative reporting.

A weekly podcast about software engineering, AI-assisted development,
and engineering leadership in the agentic era. Each episode is a solo
half-hour: a quick news segment up top, one longer essay-style argument
underneath, and one or two things the listener can actually do this
week. Every episode also ships as a written blog post on the site, for
people who'd rather read.

This repo holds everything needed to produce an episode end-to-end:
script in Markdown, blog post in Markdown, a Piper TTS pipeline that
turns the script into a single MP3, a static site generator that
publishes both the audio and the post, and an iTunes-compatible RSS
feed.

## What's in here

```
land-the-plane/
├── CLAUDE.md                    project context auto-loaded by Claude
│                                Code at session start
├── philosophies.md              editorial stance; the source of truth for
│                                the show's voice and recurring themes
├── episodes/
│   ├── INDEX.md                 topic/angle log so future episodes don't
│   │                            accidentally repeat (or knowingly revisit)
│   └── 001-intent-layer/
│       ├── script.md            spoken script (input to TTS)
│       ├── post.md              blog version (rendered on the site)
│       ├── research.md          (optional) sourced research brief — kept
│       │                        for reference if you used prompts/
│       ├── segments/            per-paragraph WAVs (intermediate, gitignored)
│       ├── episode.wav          rendered audio (intermediate, gitignored)
│       ├── episode.mp3          final audio for distribution
│       └── episode.json         metadata (title, duration, size, etc.)
├── templates/
│   └── episode_template.md      scaffold for new episodes
├── prompts/
│   ├── research_brief.md        sourced-research prompt (LLM-agnostic)
│   ├── draft_script.md          script + post drafting prompt
│   └── check_script.md          pre-render sanity-check prompt
├── .claude/commands/            slash commands for the weekly workflow
│   ├── new-episode.md
│   ├── draft-episode.md
│   ├── check-script.md
│   ├── render.md
│   └── publish.md
├── scripts/
│   ├── install_voice.sh         download the Piper voice model
│   ├── new_episode.sh           scaffold a new episode directory
│   ├── generate.py              render a script.md into MP3 + metadata
│   │                            (`--preview N` for fast iteration)
│   ├── make_cover.py            (re)generate docs/cover.png
│   ├── build_site.py            build docs/ from episodes/
│   └── release.sh               render + build + commit + push, one shot
├── docs/                        GitHub Pages source
│   ├── index.html               home page (episode list)
│   ├── cover.png                show cover art
│   ├── feed.xml                 RSS / podcast feed
│   ├── style.css
│   └── episodes/<slug>/
│       ├── index.html           blog post page
│       └── episode.mp3          audio
├── voices/                      Piper voice models (gitignored)
├── .github/workflows/pages.yml  auto-deploys docs/ to GitHub Pages
└── requirements.txt
```

## One-time setup

System packages:

```bash
sudo apt-get install -y ffmpeg espeak-ng
```

Python:

```bash
pip install -r requirements.txt
```

Voice model (~70 MB, downloaded once):

```bash
bash scripts/install_voice.sh
```

Cover art (regenerate any time the show metadata changes):

```bash
python scripts/make_cover.py
```

## The weekly workflow

### From inside Claude Code (recommended)

The fast path uses the slash commands in `.claude/commands/`:

```
/new-episode 002 new-code-review
/draft-episode 002-new-code-review "the new code review when agents write the first draft"
/check-script 002-new-code-review
/render 002-new-code-review
/publish 002-new-code-review
```

`/draft-episode` reads `philosophies.md` and `episodes/INDEX.md`,
spawns a research agent (sourced web brief), then writes both
`script.md` and `post.md` following the show's structure. Review
before rendering.

### From a regular shell (or any LLM)

The same steps without slash-command sugar:

```bash
# 1. Scaffold
bash scripts/new_episode.sh 002 new-code-review

# 2. Write the script and the post
$EDITOR episodes/002-new-code-review/script.md
$EDITOR episodes/002-new-code-review/post.md

# 3. (Optional) preview the first few paragraphs to test voice/pacing
#    without paying the full ~10 min cost
python scripts/generate.py episodes/002-new-code-review/script.md --preview 3

# 4. Render and publish in one shot
bash scripts/release.sh 002-new-code-review
```

`scripts/release.sh` runs generate.py → build_site.py → stages the
changes → shows you the diff → asks before committing and pushing.
Pass `--no-render` if you've already rendered and only want to ship
site/post edits.

### Drafting with any LLM (no Claude Code)

`prompts/` contains the canonical templates:

- `prompts/research_brief.md` — produces a sourced research brief for
  the week's topic. Output goes to `episodes/<slug>/research.md`.
- `prompts/draft_script.md` — turns `philosophies.md` + the research
  brief into a draft `script.md` and `post.md`.
- `prompts/check_script.md` — pre-render sanity check for TTS issues
  and metadata problems.

Copy any of these into a chat with any frontier model. They're
LLM-agnostic.

## Hosting on GitHub Pages

The included GitHub Action (`.github/workflows/pages.yml`) deploys
`docs/` to GitHub Pages on every push to `main` that touches the
folder. To turn this on the first time:

1. Push the repo to GitHub.
2. In the repo settings, go to **Pages**.
3. Under "Build and deployment", set **Source** to **GitHub Actions**.
4. The next push to `main` that changes `docs/` will publish.

The default site URL is `https://<owner>.github.io/<repo>/`. If you
serve from a custom domain, set `BASE_URL` when you build:

```bash
BASE_URL=https://podcast.example.com python scripts/build_site.py
```

`BASE_URL` is what shows up in the RSS `<enclosure>` URLs, so it has to
be the public URL of the site or no podcast app will find the audio.

## Subscribing

The feed lives at `<BASE_URL>/feed.xml`. Paste that URL into any
podcast app to subscribe. To list the show in Apple Podcasts, Spotify,
or Overcast, submit the feed URL through each provider's podcast
console once. After that, every new episode you push is picked up
automatically.

## Script conventions

The TTS parser in `scripts/generate.py` is intentionally simple. In a
`script.md`:

- The first `# Heading` becomes the episode title (`Episode NNN — Title`).
- A `**Key:** value` block under the heading is metadata. Supported
  keys: `Subtitle`, `Published` (YYYY-MM-DD), `Summary`. Wrapped
  multi-line values are joined.
- Everything before the first `---` is treated as metadata and not
  spoken.
- `##` headings inside the body are skipped (they're structural for
  editing, not narration).
- A line that is exactly `---` becomes a longer pause in the audio.
  Use it between major sections.
- Blank lines separate paragraphs. Each paragraph becomes one Piper
  synthesis call, which means each paragraph is its own prosodic unit
  — write them at the length you want the listener to feel.
- Numbers, dates, and abbreviations: write them as you want them
  spoken. `nineteen seventy-four`, not `1974`. `two A M`, not `2am`.
  `twenty twenty-six`, not `2026`.

The `post.md` file is rendered as regular Markdown (extras: tables,
smart quotes, sane lists). Links in `post.md` show up on the website
and in the RSS `content:encoded` body; the audio version omits them.

## Generation knobs

In `scripts/generate.py`:

- `LENGTH_SCALE` (default `1.10`) — phoneme duration multiplier.
  Higher = slower / more deliberate. `1.0` is the model's native pace
  (~210 wpm); `1.10` lands around 190 wpm.
- `SENTENCE_SILENCE` (default `0.45`s) — pause between sentences
  within a paragraph.
- `PARAGRAPH_SILENCE` (default `0.65`s) — pause between paragraphs.
- `SECTION_SILENCE` (default `1.40`s) — pause at `---` section breaks.

If an episode feels rushed, bump `LENGTH_SCALE` to `1.15` or `1.20`. If
it drags, drop it to `1.05`.

The MP3 is encoded mono at 96 kbps — clean for speech at ~12 MB per
30-minute episode. Bump in `encode_mp3()` if you want stereo or higher
quality.

## Why local TTS

[Piper](https://github.com/rhasspy/piper) runs CPU-only at roughly 3x
real-time, with no API key and no per-character billing. The default
voice is `en-US Ryan (medium)`, a male American narration voice. The
full catalogue of Piper voices is at the Piper repo — to swap voices,
update `VOICE_MODEL` in `scripts/generate.py` and the download URL in
`scripts/install_voice.sh`.

## License

Code under MIT. Episode content under CC BY 4.0 unless noted.
