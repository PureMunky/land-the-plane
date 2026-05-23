---
description: Build the site, update the index, commit, and push an episode
argument-hint: <episode-slug>
---

Publish `episodes/$ARGUMENTS/` — rebuilds the site, updates the topic
index, commits, and pushes.

Steps:

1. Verify all four expected files exist:
   - `episodes/$ARGUMENTS/script.md`
   - `episodes/$ARGUMENTS/post.md`
   - `episodes/$ARGUMENTS/episode.mp3`
   - `episodes/$ARGUMENTS/episode.json`

   If `episode.mp3` or `episode.json` is missing, tell the user to run
   `/render $ARGUMENTS` first.

2. Append a one-line entry to `episodes/INDEX.md` for this episode:
   the number, title, published date, and a one-sentence topic
   description pulled from the `Summary` in `episode.json`. Keep the
   list in reverse chronological order (newest first).

3. Run `python3 scripts/build_site.py`. This regenerates
   `docs/index.html`, the per-episode page under
   `docs/episodes/$ARGUMENTS/`, and the RSS feed.

4. Show the user `git status` and `git diff --stat`. Confirm what will
   be committed — at minimum:
   - `episodes/$ARGUMENTS/{script,post,episode.json,episode.mp3}.md`
   - `episodes/INDEX.md`
   - Everything under `docs/`

5. Commit with a message of the form:
   ```
   Episode NNN: <title>

   <one-sentence summary from episode.json>
   ```

6. Push to the current branch with `git push -u origin HEAD`.

7. Report:
   - The commit SHA
   - A reminder that GitHub Pages will redeploy when this lands on
     `main` (the action only runs on `main` for the production
     domain)
   - The likely live URL once it deploys
