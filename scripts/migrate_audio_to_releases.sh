#!/usr/bin/env bash
# One-time migration: publish each episode's audio as a GitHub Release
# asset so the RSS feed and blog can point at Release-hosted audio
# instead of committing MP3s to git / serving them from GitHub Pages.
#
# For every episodes/NNN-slug/episode.mp3 this creates (or updates) a
# release tagged `ep-NNN` with the file uploaded as `episode.mp3`, giving
# a stable URL:
#
#     https://github.com/<owner>/<repo>/releases/download/ep-NNN/episode.mp3
#
# which is exactly what scripts/build_site.py's audio_url_for() expects.
#
# Idempotent: re-running clobbers existing assets, so it is safe to run
# again. Run this BEFORE the cutover that removes episode.mp3 from git,
# because it reads the committed MP3 bytes (preserving the exact original
# audio rather than re-rendering it).
#
# Requires: gh CLI authenticated with a token that has `contents: write`
# (the migrate-audio.yml workflow supplies this automatically).

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

shopt -s nullglob
mp3s=(episodes/*/episode.mp3)
if [ ${#mp3s[@]} -eq 0 ]; then
  echo "No episodes/*/episode.mp3 found — nothing to migrate." >&2
  echo "Run this from a commit that still has the audio committed." >&2
  exit 1
fi

count=0
for mp3 in "${mp3s[@]}"; do
  dir="$(dirname "$mp3")"
  slug="$(basename "$dir")"
  num="${slug%%-*}"          # 006-cleared-to-land -> 006
  tag="ep-$num"

  title="Episode $num"
  if [ -f "$dir/episode.json" ]; then
    t="$(python3 -c "import json;print(json.load(open('$dir/episode.json')).get('title',''))" 2>/dev/null || true)"
    [ -n "$t" ] && title="Episode $num — $t"
  fi

  echo "==> $tag  <-  $mp3"
  if gh release view "$tag" >/dev/null 2>&1; then
    gh release upload "$tag" "$mp3#episode.mp3" --clobber
  else
    gh release create "$tag" "$mp3#episode.mp3" \
      --title "$title" \
      --notes "Audio enclosure for $slug, hosted as a Release asset so the podcast feed and blog can link here instead of committing audio to git."
  fi
  count=$((count + 1))
done

echo "Migrated $count episode(s) to Releases."
