# Draft prompt

Use this prompt to turn the research brief + `philosophies.md` into a
draft `script.md` and `post.md` for a Land the Plane episode.

Drop it into any frontier LLM with file access (Claude Code, Codex,
etc.) after putting the research brief at
`episodes/<slug>/research.md`.

---

## Prompt

You are drafting episode `<NNN>` of Land the Plane. The slug is
`<slug>`. The publish date is `<YYYY-MM-DD>`.

Before you write a word, read these three files end to end:

1. `CLAUDE.md` — project context, hard rules, conventions.
2. `philosophies.md` — voice, recurring themes, editorial stance.
3. `episodes/<slug>/research.md` — the sourced research brief for
   this week.

Then read at least one prior episode's `script.md` and `post.md` for
tone calibration. The most recent one is fine.

Now produce two files.

### `episodes/<slug>/script.md` — the spoken version

Length target: 4,800–5,200 words of body content (~27–30 minutes at
the default `LENGTH_SCALE=1.10` ≈ 190 wpm).

Required structure (top to bottom):

1. **Frontmatter block** — `# Episode NNN — Title`, then a metadata
   block with `**Subtitle:**`, `**Published:**`, and `**Summary:**`
   keys. Summary should be 2-4 sentences and read well as the show
   notes on the site and in the RSS feed. Close with a `---`.

2. **Show open** — `## Show open`. About 100 words. Introduces the
   show, reminds the listener of the format (news + main piece +
   takeaway), thanks them for being there. Voice should sound like
   the host has done this 50 times even if it's episode 2.

3. **This week on the radar** — `## This week on the radar`. 3-4
   news items from the research brief. ~600-800 words. For each
   item: name the thing, ground it in a date and a source, give the
   host's one-line take. Close with a transition into the main
   piece.

4. **Cold open** — `## Cold open`. 300-400 words. A scene, a
   tension, or a question that grounds the abstract argument in
   something concrete. Hand off into the main piece in the last
   paragraph.

5. **Main piece** — usually three `##` sections separated by `---`.
   ~3,000-3,500 words total. Each section is its own beat of the
   argument; the third should be the most consequential. End the
   piece with a one-line summary of the thesis.

6. **Close** — `## Close`. 400-600 words. Two or three concrete
   things the listener can do this week. Tie back to the cold open
   if you can.

7. **Sign-off** — `## Sign-off`. ~100 words. Tease next week if you
   have a thread; end with "This has been Land the Plane."

**TTS conventions to follow throughout the script:**

- Spell numbers, years, times: `nineteen seventy-four`, `twenty
  twenty-six`, `two A M`, `ninety-six kilobits`, not their digit
  forms.
- Spell percentages: `nineteen percent`, not `19%`.
- Surround em-dashes with spaces — like this — for cleaner Piper
  prosody.
- Avoid parenthetical asides — TTS doesn't lower its voice for
  them. Recast as a separate sentence.
- One paragraph per prosodic unit. Short standalone sentences land
  hard; use them deliberately at the climax of an argument.
- No Markdown tables, no code fences, no inline links — the audio
  version doesn't carry hyperlinks.
- Pronounce-tricky abbreviations should be spelled phonetically the
  first time. `RBAC` becomes `R-bac` or just write it as `role-
  based access control`.

### `episodes/<slug>/post.md` — the blog version

Same arguments, written for a reader. Length target: 3,000-4,500
words. Differences from the script:

- Title is the same. Open with the subtitle as italic kicker, then a
  one-line note that "the audio version of this piece is [Claude
  Cast episode N](./episode.mp3); this post covers the same ground
  for people who'd rather read." Then `---`.
- Mirror the news segment but with inline hyperlinks to every source
  in the research brief.
- Mirror the cold open and the main piece. Allow yourself slightly
  denser prose since the reader controls the pace.
- Use `##` subheadings for navigation.
- The "What to do this week" section is the same set of action
  items but can be a numbered list with bolded leads.
- End with a `## Sources` section: bulleted list of every URL cited
  in the post.

### Hard rules (from `CLAUDE.md`)

- **Never mention the host's employment** (current or past employers,
  job titles tied to employers). The host's experience is perspective,
  not autobiography.
- The audience is other engineers and managers, not the host's diary.
- Avoid corporate-generic language. If a sentence could appear in any
  LinkedIn post, rewrite it.
- Don't quote at length without attribution and a source. Don't make
  up quotes.

### When you're done

Report back with:

- Word count of script body (excluding frontmatter and `##` headings).
- Estimated audio duration at 190 wpm.
- A one-paragraph summary of the argument.
- Anything you cut from the research brief and why.
- Anything you think is weak and want the host to look at before
  rendering.

Do not render audio. Do not commit. Just write the two files and
report.
