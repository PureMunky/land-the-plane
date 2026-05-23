---
description: Research a topic and draft the script + blog post for an episode
argument-hint: <episode-slug> "<topic and angle>"
---

Draft a full Claude Cast episode (script + blog post) on the topic
the user has supplied.

Arguments: `$ARGUMENTS` — expect `<episode-slug>` (e.g. `002-new-code-review`)
followed by a quoted topic and angle.

Before drafting, you MUST do these in order:

1. **Read [`CLAUDE.md`](../../CLAUDE.md) and
   [`philosophies.md`](../../philosophies.md).** Both are short. They
   set voice, format, and hard rules (e.g. never mention the host's
   employment).

2. **Read [`episodes/INDEX.md`](../../episodes/INDEX.md)** to make
   sure this topic hasn't already been covered. If it has been
   covered, tell the user and ask whether to skip, revisit from a new
   angle, or proceed anyway.

3. **Read at least one prior episode's `script.md` and `post.md`**
   for tone calibration. The most recent one is fine.

4. **Read [`prompts/research_brief.md`](../../prompts/research_brief.md)
   and [`prompts/draft_script.md`](../../prompts/draft_script.md)** —
   these are the canonical templates for the steps below. Follow them.

Then:

5. **Launch a research agent in the background** using the prompt in
   `prompts/research_brief.md`, with the topic from `$ARGUMENTS`
   substituted in. Use the `general-purpose` agent type. Keep doing
   structural work (file scaffolding, script outline) while it runs.

6. **When the research returns, draft both files** following the
   instructions in `prompts/draft_script.md`:
   - `episodes/<slug>/script.md` — the spoken version, with the
     correct frontmatter (Subtitle / Published / Summary), an honest
     news-of-the-week section sourced from the research, a cold open,
     a three-act-or-similar main piece, and a closing call to action.
     Use TTS conventions (spelled numbers, spaced em-dashes).
   - `episodes/<slug>/post.md` — the same argument as essay prose for
     readers, with inline hyperlinks to every source from the
     research brief. Often tighter than the script.

7. **Report back** with:
   - Word count for the script and estimated audio duration
     (~190 wpm at the default `LENGTH_SCALE=1.10`).
   - One-paragraph summary of the argument.
   - Any open questions or weak points you want the user to look at
     before rendering.

Do NOT render audio or commit anything in this command — that's
`/render` and `/publish`. This command produces drafts the user can
edit before paying the 10-minute TTS cost.
