#!/usr/bin/env bash
# Render, build, commit, and push an episode in one shot.
#
# Usage: scripts/release.sh <episode-slug>
# Example: scripts/release.sh 002-new-code-review
#
# Assumes scripts/generate.py has not yet been run (or that you want to
# re-render). If you've already run generate.py and just want to publish
# the site changes, pass --no-render.
set -euo pipefail

SLUG="${1:-}"
NO_RENDER=0
for arg in "${@:2}"; do
    case "$arg" in
        --no-render) NO_RENDER=1 ;;
        *) echo "Unknown option: $arg" >&2; exit 1 ;;
    esac
done

if [[ -z "$SLUG" ]]; then
    echo "Usage: $0 <episode-slug> [--no-render]" >&2
    echo "Example: $0 002-new-code-review" >&2
    exit 1
fi

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
EP_DIR="$ROOT/episodes/$SLUG"

if [[ ! -d "$EP_DIR" ]]; then
    echo "No such episode: $EP_DIR" >&2
    exit 1
fi
if [[ ! -f "$EP_DIR/script.md" ]]; then
    echo "Missing $EP_DIR/script.md" >&2
    exit 1
fi
if [[ ! -f "$EP_DIR/post.md" ]]; then
    echo "Missing $EP_DIR/post.md" >&2
    exit 1
fi

cd "$ROOT"

if [[ $NO_RENDER -eq 0 ]]; then
    echo "==> Rendering audio (this takes ~10 min for a 30-min episode)"
    python3 scripts/generate.py "$EP_DIR/script.md"
fi

if [[ ! -f "$EP_DIR/episode.mp3" || ! -f "$EP_DIR/episode.json" ]]; then
    echo "Render did not produce episode.mp3 / episode.json — aborting" >&2
    exit 1
fi

echo "==> Building site"
python3 scripts/build_site.py

# Pull title + summary out of episode.json for the commit message
TITLE=$(python3 -c "import json,sys;m=json.load(open('$EP_DIR/episode.json'));print(m.get('title',''))")
NUMBER=$(python3 -c "import json,sys;m=json.load(open('$EP_DIR/episode.json'));print(f\"{m.get('number',0):03d}\")")
SUMMARY=$(python3 -c "import json,sys;m=json.load(open('$EP_DIR/episode.json'));print(m.get('summary','')[:240])")

echo "==> Staging changes"
git add "$EP_DIR" docs episodes/INDEX.md 2>/dev/null || true

if git diff --cached --quiet; then
    echo "Nothing to commit." >&2
    exit 0
fi

git status --short
echo
echo "==> Commit message preview:"
echo "Episode $NUMBER: $TITLE"
echo
echo "$SUMMARY"
echo

read -r -p "Commit and push? [y/N] " yn
case "$yn" in
    y|Y) ;;
    *) echo "Aborted (changes left staged)."; exit 0 ;;
esac

git commit -m "Episode $NUMBER: $TITLE

$SUMMARY"
git push -u origin HEAD
echo "==> Done. GitHub Pages will redeploy when this lands on main."
