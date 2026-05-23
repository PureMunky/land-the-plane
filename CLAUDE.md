# Land the Plane — project context

This file is read automatically by Claude Code at the start of any
session in this repo. It is the orientation any agent needs before
touching content or running the pipeline.

## What this repo is

Land the Plane is a weekly solo half-hour podcast about software
engineering, AI-assisted development, and engineering leadership in
the agentic era. Every episode ships as both audio (rendered locally
with Piper TTS) and a written blog post (rendered to the GitHub Pages
site at `docs/`), plus an iTunes-format RSS feed for subscribers.

The repo is fully self-contained — scripts, audio, site, and feed all
live here and ship together.

## Editorial stance

The single source of truth for voice, format, and recurring themes is
[`philosophies.md`](./philosophies.md). **Read it before drafting any
content.** Update it when the editorial direction shifts; the next
draft will pull from the new version.

Hard rules that apply to anything published from this repo:

- **Never mention the host's employment history** (current or past
  employers, job titles tied to employers). The host's experience
  appears as perspective and opinion, never as autobiography or name-
  checking.
- The voice is opinionated and plain-spoken. Avoid corporate-generic
  language ("leverage," "synergy," "ensure that," "going forward,"
  "best practices").
- The audience is other engineers and engineering managers — not just
  the host. Write for someone who wants to learn or argue, not for the
  host's diary.

## File conventions

Each episode lives in `episodes/NNN-slug/` and contains:

- `script.md` — what the TTS reads. Input to `scripts/generate.py`.
- `post.md` — the blog version. Rendered as HTML by
  `scripts/build_site.py`. Often more sources/links than the script,
  often slightly tighter prose (the reader is faster than the
  listener).
- `episode.mp3` — distribution audio (written by generate.py).
- `episode.json` — metadata (written by generate.py).
- `segments/` — per-paragraph intermediate WAVs. Gitignored; safe to
  delete.

### Script frontmatter

Every `script.md` opens with:

```markdown
# Episode NNN — Title

**Subtitle:** One-line topic line.
**Published:** YYYY-MM-DD
**Summary:** A paragraph (can wrap across lines) used as the show
notes in the RSS feed and the episode card on the home page.

---
```

The parser in `scripts/generate.py` treats everything before the first
`---` as metadata and skips it; everything after is the spoken body.

### TTS conventions in the script

- Spell numbers, years, and times: `nineteen seventy-four`, not
  `1974`; `two A M`, not `2am`; `twenty twenty-six`, not `2026`.
- Surround em-dashes with spaces — like this — for cleaner Piper
  prosody.
- Each blank-line paragraph becomes one Piper invocation, which is
  also one prosodic unit. Length paragraphs the way you want them
  felt; short standalone lines land hard.
- Section breaks (`---` on its own line) insert a longer pause.

## The weekly workflow

The fastest path from "I want to do this week's episode" to "it's
live":

```bash
/new-episode 002 new-code-review
/draft-episode 002-new-code-review "the new code review when agents write the first draft"
# review and edit episodes/002-new-code-review/{script,post}.md
/check-script 002-new-code-review
/render 002-new-code-review
/publish 002-new-code-review
```

Each slash command is defined in `.claude/commands/` — open the file
to see what it does.

For non-Claude usage (or scripting), the same flow with bash:

```bash
bash scripts/new_episode.sh 002 new-code-review
# (write the content yourself or with whatever LLM you prefer; see
#  prompts/ for the research and draft templates)
python scripts/generate.py episodes/002-new-code-review/script.md
bash scripts/release.sh 002-new-code-review
```

## Prompts library

`prompts/` holds the prompt templates that produced this show's first
episode and are intended to be reused weekly. They are deliberately
LLM-agnostic — copy them into any chat with any frontier model.

- `prompts/research_brief.md` — produces a sourced research brief on a
  week's topic, in the form the drafting prompt expects as input.
- `prompts/draft_script.md` — turns `philosophies.md` + the research
  brief into a `script.md` + `post.md` draft.
- `prompts/check_script.md` — heuristics for catching TTS-unfriendly
  patterns and metadata issues in a draft script.

## What's been covered

See [`episodes/INDEX.md`](./episodes/INDEX.md) before pitching a new
topic. The index lists topic, angle, and key sources for every
published episode so we don't accidentally repeat ourselves (or so we
deliberately revisit a topic from a different angle, knowing it's a
revisit).

## What to never auto-commit

- Voice models (`voices/*.onnx*`) — large, reproducible via
  `scripts/install_voice.sh`.
- Intermediate WAVs (`episodes/*/segments/`, `episodes/*/episode.wav`)
  — large, reproducible from `script.md`.

The `.gitignore` already handles these; don't loosen it without a
reason.
