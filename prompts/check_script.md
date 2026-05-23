# Check-script prompt

Heuristics for catching TTS-unfriendly patterns and metadata issues in
a draft `script.md`. Used by the `/check-script` slash command but
written generically so it works in any LLM context.

---

## Prompt

Read `episodes/<slug>/script.md` and audit it for problems that will
hurt the rendered audio or break the site build. Be specific — quote
the offending text and give the line number where you can.

### TTS-killer issues (high priority)

- **Bare digits.** Years (`1974`, `2026`), times (`2am`, `2 PM`),
  version numbers, percentages (`19%`), dollar amounts (`$500`).
  Piper says `1974` as "one nine seven four"; the right form is
  `nineteen seventy-four`.
- **Abbreviations that don't pronounce naturally** as either letters
  or words. `AI`, `API`, `URL`, `CI/CD`, `PR` all read fine. `RHEL`,
  `RBAC`, `SLO` don't — spell phonetically or expand.
- **Symbols Piper mispronounces.** `&`, `/`, `<`, `>`, `~`, `*`, raw
  math operators, anything in backticks.
- **Inline Markdown the script parser doesn't strip:** tables, raw
  HTML, code fences.

### Frontmatter issues (will break the site build)

- Missing `# Episode NNN — Title` heading on line 1.
- Missing `**Subtitle:**`, `**Published:**`, or `**Summary:**` lines.
- `Published` not in `YYYY-MM-DD` form.
- Frontmatter that lives AFTER the first `---` (it will be parsed as
  body and synthesized into audio).

### Editorial issues (per CLAUDE.md hard rules)

- Any reference to the host's employment (current or past employers,
  job titles tied to employers).
- Corporate-generic phrases the show avoids: "leverage," "synergy,"
  "best practices," "ensure that," "going forward," "circle back,"
  "double-click on," "at the end of the day."
- Paragraphs over ~200 words. Piper handles them but the listener
  loses the prosody anchor.

### Length sanity check

- Word count of the body (everything after the first `---`, excluding
  `##` heading lines and metadata).
- Estimated audio duration at `LENGTH_SCALE=1.10` → ~190 wpm.
- Flag if duration is under 20 minutes or over 40 minutes.

### Output

If you find issues, list them grouped by category, with quotes and
line numbers. If you find nothing, say so explicitly and report the
word count + estimated duration so the host knows the script is
ready to render. Do NOT modify the script — only report.
