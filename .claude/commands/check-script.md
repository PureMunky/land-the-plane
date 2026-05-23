---
description: Sanity-check a script.md for TTS issues and metadata problems
argument-hint: <episode-slug>
---

Audit `episodes/$ARGUMENTS/script.md` for problems that will hurt the
rendered audio or break the site build.

Read the script and report any of the following you find. Be specific
— quote the offending text and give the line number.

**TTS-killer issues** (high priority):
- Bare digits where the audio needs words. Years (`1974`, `2026`),
  times (`2am`, `2 PM`), version numbers, percentages with `%`,
  dollar amounts with `$`. Piper will pronounce `1974` as "one nine
  seven four"; spell `nineteen seventy-four`.
- Abbreviations that don't pronounce naturally as letters or words.
  E.g. `CI/CD` reads OK; `RHEL` doesn't; `AI` and `URL` are fine;
  `RBAC` is iffy.
- Symbols and punctuation that Piper mispronounces: `&` (reads as
  "and" — usually fine, sometimes wrong), `/`, `<`, `>`, `~`, math
  operators.
- Inline Markdown the script parser doesn't strip: tables, raw HTML,
  code fences.

**Frontmatter issues** (will break the site build):
- Missing `# Episode NNN — Title` heading.
- Missing `**Subtitle:**`, `**Published:**`, or `**Summary:**` lines.
- `Published` value that isn't `YYYY-MM-DD`.
- Frontmatter that appears AFTER the first `---` line (parser will
  skip it and the metadata will be empty).

**Editorial issues** (per `CLAUDE.md` rules):
- Any reference to the host's employment (current or past employers,
  or job titles tied to an employer).
- Corporate-generic phrases the show explicitly avoids: "leverage,"
  "synergy," "best practices," "ensure that," "going forward,"
  "circle back," "double-click on."
- Paragraphs over ~200 words (Piper handles them but the listener
  loses the prosody anchor).

**Length sanity check:**
- Word count of the body (excluding frontmatter and `##` headings).
- Estimated audio duration at `LENGTH_SCALE=1.10` → ~190 wpm.
- Flag if duration is less than 20 minutes or more than 40 minutes.

If you find nothing, say so explicitly and report the word count and
estimated duration. Do NOT modify the script — only report.
