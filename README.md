# Claude Cast

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
claude-cast/
├── philosophies.md              editorial stance; the source of truth for
│                                the show's voice and recurring themes
├── episodes/
│   └── 001-intent-layer/
│       ├── script.md            spoken script (input to TTS)
│       ├── post.md              blog version (rendered on the site)
│       ├── segments/            per-paragraph WAVs (intermediate)
│       ├── episode.wav          rendered audio (intermediate)
│       ├── episode.mp3          final audio for distribution
│       └── episode.json         metadata (title, duration, size, etc.)
├── templates/
│   └── episode_template.md      scaffold for new episodes
├── scripts/
│   ├── install_voice.sh         download the Piper voice model
│   ├── new_episode.sh           scaffold a new episode directory
│   ├── generate.py              render a script.md into MP3 + metadata
│   ├── make_cover.py            (re)generate docs/cover.png
│   └── build_site.py            build docs/ from episodes/
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

```bash
# 1. Scaffold the new episode
bash scripts/new_episode.sh 002 new-code-review

# 2. Write the script and the post
$EDITOR episodes/002-new-code-review/script.md
$EDITOR episodes/002-new-code-review/post.md   # copy script.md as a starting point

# 3. Render the audio (~10 min wall-clock for a 30-min episode)
python scripts/generate.py episodes/002-new-code-review/script.md

# 4. Rebuild the site
python scripts/build_site.py

# 5. Commit and push — the GitHub Action publishes docs/ to Pages
git add episodes/002-new-code-review docs
git commit -m "Episode 002: the new code review"
git push
```

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
