#!/usr/bin/env python3
"""Ensure the GitHub labels used by an episode's "comment" link exist.

Each episode page links to GitHub's new-issue screen with labels
pre-filled (see scripts/build_site.py:new_issue_url). GitHub applies
those labels only if they already exist in the repo, so we create them
at publish time.

For episode NNN with topics [a, b, ...] this ensures:
    episode-comment    stable label shared by every episode comment
    episode-NNN        per-episode label
    topic:<slug>       one per declared topic

Usage:
    python3 scripts/ensure_labels.py episodes/003-new-code-review
    python3 scripts/ensure_labels.py episodes/003-new-code-review/episode.json

Requires the GitHub CLI (`gh`), authenticated against the repo. If `gh`
is missing or a label can't be created, this prints a warning and still
exits 0 so it never blocks a release — the comment links keep working,
the labels just won't auto-apply until the labels exist.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


def topic_label(topic: str) -> str:
    """Slugify a topic into a label name. Keep in sync with
    scripts/build_site.py:topic_label."""
    slug = re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")
    return f"topic:{slug}" if slug else ""


def labels_for(meta: dict) -> list[tuple[str, str, str]]:
    """Return (name, color, description) for every label this episode needs."""
    n = meta.get("number", 0)
    title = meta.get("title", "")
    ep_desc = f"Comments on episode {n:03d}"
    if title:
        ep_desc += f" — {title}"
    labels = [
        ("episode-comment", "1d76db", "Listener comment on an episode"),
        (f"episode-{n:03d}", "c780ff", ep_desc),
    ]
    for topic in meta.get("topics", []) or []:
        name = topic_label(topic)
        if name:
            labels.append((name, "0e8a16", f"Topic: {topic}"))
    return labels


def resolve_meta_path(arg: str) -> Path:
    p = Path(arg)
    return p / "episode.json" if p.is_dir() else p


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("Usage: ensure_labels.py <episode-dir|episode.json>",
              file=sys.stderr)
        return 2

    meta_path = resolve_meta_path(argv[0])
    if not meta_path.exists():
        print(f"No episode.json at {meta_path} "
              f"(run scripts/generate.py first)", file=sys.stderr)
        return 1

    if shutil.which("gh") is None:
        print("warning: gh CLI not found; skipping label creation. "
              "Install + auth gh, then re-run "
              f"`python3 scripts/ensure_labels.py {argv[0]}`.",
              file=sys.stderr)
        return 0

    meta = json.loads(meta_path.read_text())
    failures = 0
    for name, color, desc in labels_for(meta):
        # --force updates an existing label's color/description, so this
        # is fully idempotent and safe to re-run on every publish.
        result = subprocess.run(
            ["gh", "label", "create", name,
             "--color", color, "--description", desc, "--force"],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            print(f"  ensured label {name}")
        else:
            failures += 1
            print(f"  warning: could not ensure label {name}: "
                  f"{result.stderr.strip()}", file=sys.stderr)

    if failures:
        print(f"warning: {failures} label(s) could not be ensured; the "
              "comment links still work, labels just won't auto-apply.",
              file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
