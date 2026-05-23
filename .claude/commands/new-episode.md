---
description: Scaffold a new episode directory from the template
argument-hint: <number> <slug>
---

Scaffold a new episode for Land the Plane.

Arguments: `$ARGUMENTS` — expect `<number> <slug>`, e.g. `002 new-code-review`.

Steps:
1. Run `bash scripts/new_episode.sh $ARGUMENTS` from the repo root.
2. Confirm `episodes/NNN-slug/script.md` exists.
3. Report the path back, and tell the user the next step is either
   `/draft-episode NNN-slug "<topic>"` (to have me research and draft)
   or just opening `script.md` and writing it themselves.

If the directory already exists, the script will refuse to overwrite —
don't try to force it. Tell the user and stop.
