#!/usr/bin/env bash
# Scaffold a new episode directory from the template.
#
# Usage: scripts/new_episode.sh 002 "Short slug here"
set -euo pipefail

if [[ $# -lt 2 ]]; then
    echo "Usage: $0 <number> <slug>"
    echo "Example: $0 002 new-code-review"
    exit 1
fi

NUM="$1"
SLUG="$2"
ROOT="$(dirname "$0")/.."
DEST="$ROOT/episodes/${NUM}-${SLUG}"
TEMPLATE="$ROOT/templates/episode_template.md"

if [[ -e "$DEST" ]]; then
    echo "Refusing to overwrite existing $DEST"
    exit 1
fi

mkdir -p "$DEST/segments"
cp "$TEMPLATE" "$DEST/script.md"
echo "Created $DEST/script.md"
echo "Edit the script, then run: python scripts/generate.py $DEST/script.md"
