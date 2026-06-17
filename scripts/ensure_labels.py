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
    python3 scripts/ensure_labels.py episodes/003-new-code-review [more...]
    python3 scripts/ensure_labels.py episodes/003-new-code-review/episode.json

Two backends, picked automatically:
  * REST API — used when a token is in the environment (GITHUB_TOKEN or
    GH_TOKEN). This is how the labels workflow creates them server-side
    on every push, so publishing from an environment without `gh` (such
    as Claude Code on the web) still gets labels. The repo comes from
    GITHUB_REPOSITORY, falling back to DEFAULT_REPO.
  * gh CLI — used for local publishing when no token is set but `gh` is
    installed and authenticated.

If neither is available, this prints a warning and exits 0 so it never
blocks a release — the comment links keep working, the labels just
won't auto-apply until they exist.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

# Keep in sync with scripts/build_site.py:GITHUB_REPO.
DEFAULT_REPO = "puremunky/land-the-plane"


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


# --- backends ---------------------------------------------------------------

def ensure_via_gh(name: str, color: str, desc: str) -> tuple[bool, str]:
    # --force updates an existing label's color/description, so this is
    # fully idempotent and safe to re-run on every publish.
    result = subprocess.run(
        ["gh", "label", "create", name,
         "--color", color, "--description", desc, "--force"],
        capture_output=True, text=True,
    )
    return result.returncode == 0, result.stderr.strip()


def _api_request(method: str, url: str, token: str, payload: dict):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("Content-Type", "application/json")
    return urllib.request.urlopen(req)


def ensure_via_api(repo: str, token: str):
    base = f"https://api.github.com/repos/{repo}/labels"

    def ensure(name: str, color: str, desc: str) -> tuple[bool, str]:
        body = {"name": name, "color": color, "description": desc}
        try:
            _api_request("POST", base, token, body)
            return True, ""
        except urllib.error.HTTPError as e:
            if e.code == 422:  # already exists — update color/description
                url = f"{base}/{urllib.parse.quote(name)}"
                try:
                    _api_request("PATCH", url, token,
                                 {"new_name": name, "color": color,
                                  "description": desc})
                    return True, ""
                except urllib.error.HTTPError as e2:
                    return False, f"{e2.code} {e2.read().decode()[:200]}"
            return False, f"{e.code} {e.read().decode()[:200]}"
        except urllib.error.URLError as e:
            return False, str(e.reason)

    return ensure


# --- driver -----------------------------------------------------------------

def main(argv: list[str]) -> int:
    if not argv:
        print("Usage: ensure_labels.py <episode-dir|episode.json> [more...]",
              file=sys.stderr)
        return 2

    meta_paths = [resolve_meta_path(a) for a in argv]
    missing = [str(p) for p in meta_paths if not p.exists()]
    if missing:
        print(f"No episode.json at: {', '.join(missing)} "
              f"(run scripts/generate.py first)", file=sys.stderr)
        return 1

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        repo = os.environ.get("GITHUB_REPOSITORY") or DEFAULT_REPO
        ensure = ensure_via_api(repo, token)
        print(f"Ensuring labels via GitHub API on {repo}")
    elif shutil.which("gh") is not None:
        ensure = ensure_via_gh
        print("Ensuring labels via gh CLI")
    else:
        print("warning: no GITHUB_TOKEN and no gh CLI; skipping label "
              "creation. The comment links still work; labels just won't "
              "auto-apply until they exist.", file=sys.stderr)
        return 0

    # De-duplicate across episodes so shared labels (episode-comment,
    # repeated topics) are only touched once.
    seen: set[str] = set()
    failures = 0
    for meta_path in meta_paths:
        meta = json.loads(meta_path.read_text())
        for name, color, desc in labels_for(meta):
            if name in seen:
                continue
            seen.add(name)
            ok, err = ensure(name, color, desc)
            if ok:
                print(f"  ensured label {name}")
            else:
                failures += 1
                print(f"  warning: could not ensure label {name}: {err}",
                      file=sys.stderr)

    if failures:
        print(f"warning: {failures} label(s) could not be ensured; the "
              "comment links still work, labels just won't auto-apply.",
              file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
