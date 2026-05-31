#!/usr/bin/env python3
"""Build the static site and RSS feed from the episodes/ directory.

For each episode directory `episodes/NNN-slug/` we expect:
    script.md      the spoken script (used for TTS, not rendered)
    post.md        the blog/essay version of the same material
    episode.mp3    the rendered audio (produced by scripts/generate.py)
    episode.json   metadata (also produced by scripts/generate.py)

This script emits:
    docs/index.html                       home page (episode list)
    docs/style.css                        shared stylesheet
    docs/feed.xml                         podcast-format RSS feed
    docs/episodes/NNN-slug/index.html     blog post page (per episode)
    docs/episodes/NNN-slug/episode.mp3    copy of the audio (for hosting)

The site is designed to be served by GitHub Pages from the docs/ folder
on the default branch. Set BASE_URL via environment to override the
absolute URL used in the RSS enclosures.
"""
from __future__ import annotations

import html
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path

import markdown

ROOT = Path(__file__).parent.parent
EPISODES_DIR = ROOT / "episodes"
DOCS_DIR = ROOT / "docs"

# Override at build time: BASE_URL=https://example.com/foo python scripts/build_site.py
BASE_URL = os.environ.get(
    "BASE_URL", "https://puremunky.github.io/land-the-plane"
).rstrip("/")

SHOW = {
    "title": "Land the Plane",
    "tagline": "Software engineering, AI-assisted development, and what it "
               "actually takes to lead engineering teams in the agentic era.",
    "description": (
        "A weekly half-hour about software engineering, AI-assisted "
        "development, and engineering leadership. Each episode pairs a "
        "current-events segment with one longer essay-style argument and "
        "one or two things you can actually do this week. "
        "Experimental: every episode is researched, drafted, and "
        "audio-rendered end-to-end through an AI pipeline, with a "
        "synthetic voice (Piper TTS). Treat episodes as working drafts."
    ),
    "experimental_notice": (
        "Every episode is researched, drafted, and audio-rendered "
        "end-to-end through an AI pipeline. The voice is synthetic "
        "(Piper TTS). Treat episodes as working drafts of an argument, "
        "not authoritative reporting."
    ),
    "language": "en-us",
    "author": "Land the Plane",
    "email": "phil@philcorbett.net",  # iTunes/YouTube owner-verification address
    "category": "Technology",
    "explicit": "false",
    "copyright": f"© {datetime.now(timezone.utc).year} Land the Plane",
}

STYLE_CSS = """
:root {
  --bg: #0e1119;
  --surface: #161b27;
  --text: #e8ebf2;
  --muted: #9aa3b8;
  --accent: #c780ff;
  --rule: #232a3a;
  --link: #8fb8ff;
}
* { box-sizing: border-box; }
html, body {
  margin: 0; padding: 0;
  background: var(--bg);
  color: var(--text);
  font: 17px/1.6 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
        "Helvetica Neue", Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
}
a { color: var(--link); }
a:hover { color: var(--accent); }
.container { max-width: 720px; margin: 0 auto; padding: 48px 24px 96px; }
.site-header { display: flex; align-items: center; gap: 16px; margin-bottom: 8px; }
.site-header img { width: 64px; height: 64px; border-radius: 12px; }
.site-header h1 { font-size: 24px; margin: 0; letter-spacing: -0.01em; }
.site-header a { color: var(--text); text-decoration: none; }
.site-tagline { color: var(--muted); margin: 4px 0 16px; }
.experiment-notice {
  background: rgba(199, 128, 255, 0.08);
  border: 1px solid rgba(199, 128, 255, 0.25);
  border-radius: 10px;
  padding: 12px 16px;
  font-size: 14px;
  color: var(--muted);
  margin: 16px 0 24px;
}
.experiment-notice strong { color: var(--accent); }
.nav-links { margin: 8px 0 40px; display: flex; gap: 16px; font-size: 14px; }
.nav-links a { color: var(--muted); text-decoration: none; }
.nav-links a:hover { color: var(--accent); }
h2 { font-size: 22px; letter-spacing: -0.01em; margin: 40px 0 8px; }
h3 { font-size: 18px; margin: 32px 0 8px; }
.episode-card {
  display: block;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 12px;
  padding: 24px 28px;
  margin: 20px 0;
  text-decoration: none;
  color: var(--text);
  transition: transform 0.15s ease, border-color 0.15s ease;
}
.episode-card:hover {
  transform: translateY(-2px);
  border-color: var(--accent);
}
.episode-meta {
  display: flex; gap: 12px;
  font-size: 13px;
  color: var(--muted);
  margin-bottom: 6px;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.episode-card h2 { margin: 0 0 8px; font-size: 22px; }
.episode-card .subtitle { color: var(--muted); margin: 4px 0 12px; font-style: italic; }
.episode-card .summary { color: var(--text); margin: 0; }
audio { width: 100%; margin: 24px 0; }
article p { margin: 14px 0; }
article ul, article ol { padding-left: 22px; }
article li { margin: 6px 0; }
article blockquote {
  border-left: 3px solid var(--accent);
  margin: 18px 0;
  padding: 4px 18px;
  color: var(--muted);
}
article hr { border: 0; border-top: 1px solid var(--rule); margin: 36px 0; }
.back-link {
  display: inline-block;
  margin-top: 32px;
  color: var(--muted);
  text-decoration: none;
}
.back-link:hover { color: var(--accent); }
footer {
  margin-top: 80px;
  padding-top: 24px;
  border-top: 1px solid var(--rule);
  font-size: 14px;
  color: var(--muted);
}
"""


def discover_episodes() -> list[dict]:
    """Return episodes sorted newest-first by published date."""
    episodes = []
    for ep_dir in sorted(EPISODES_DIR.iterdir()):
        if not ep_dir.is_dir():
            continue
        meta_path = ep_dir / "episode.json"
        if not meta_path.exists():
            print(f"  skip {ep_dir.name}: no episode.json "
                  f"(run scripts/generate.py first)")
            continue
        meta = json.loads(meta_path.read_text())
        meta["_dir"] = ep_dir
        meta["_post_path"] = ep_dir / "post.md"
        meta["_mp3_path"] = ep_dir / "episode.mp3"
        episodes.append(meta)

    episodes.sort(key=lambda m: m.get("published", "0000"), reverse=True)
    return episodes


def render_layout(title: str, body: str, *, is_root: bool = False) -> str:
    """Wrap a body in the shared shell."""
    home_href = "./" if is_root else "../../"
    feed_href = "./feed.xml" if is_root else "../../feed.xml"
    cover_href = "./cover.png" if is_root else "../../cover.png"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{'./style.css' if is_root else '../../style.css'}">
<link rel="alternate" type="application/rss+xml" title="Land the Plane" href="{feed_href}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:type" content="website">
<meta property="og:image" content="{BASE_URL}/cover.png">
</head>
<body>
<div class="container">
<header class="site-header">
<a href="{home_href}"><img src="{cover_href}" alt=""></a>
<a href="{home_href}"><h1>{SHOW['title']}</h1></a>
</header>
<p class="site-tagline">{html.escape(SHOW['tagline'])}</p>
<aside class="experiment-notice">
<strong>Experimental.</strong> {html.escape(SHOW['experimental_notice'])}
</aside>
<nav class="nav-links">
  <a href="{home_href}">Episodes</a>
  <a href="{feed_href}">RSS</a>
  <a href="https://github.com/puremunky/land-the-plane">GitHub</a>
</nav>
{body}
<footer>
<p>Land the Plane is rendered with local TTS from
<a href="https://github.com/puremunky/land-the-plane">this open repo</a>.
Subscribe in any podcast app via <a href="{feed_href}">the RSS feed</a>.</p>
</footer>
</div>
</body>
</html>
"""


def render_home(episodes: list[dict]) -> str:
    cards = []
    for ep in episodes:
        n = ep.get("number", 0)
        date = ep.get("published", "")
        dur = ep.get("duration_hms", "")
        meta_line = " · ".join(
            x for x in [f"Episode {n:03d}", date, dur] if x
        )
        href = f"./episodes/{ep['slug']}/"
        cards.append(f"""
<a class="episode-card" href="{href}">
<div class="episode-meta">{html.escape(meta_line)}</div>
<h2>{html.escape(ep.get('title', '(untitled)'))}</h2>
<p class="subtitle">{html.escape(ep.get('subtitle', ''))}</p>
<p class="summary">{html.escape(ep.get('summary', ''))}</p>
</a>""")
    body = "<h2>Latest episodes</h2>" + "\n".join(cards) if cards else (
        "<p>No episodes yet. Run "
        "<code>python scripts/generate.py episodes/&lt;slug&gt;/script.md</code>"
        " and rebuild.</p>"
    )
    return render_layout(SHOW["title"], body, is_root=True)


def render_episode_page(ep: dict) -> str:
    md_text = ep["_post_path"].read_text(encoding="utf-8")
    body_html = markdown.markdown(
        md_text,
        extensions=["extra", "smarty", "sane_lists"],
    )
    audio_url = f"./episode.mp3"
    audio_block = (
        f'<audio controls preload="metadata" src="{audio_url}"></audio>'
    )
    article = f"""
<p class="episode-meta">Episode {ep.get('number', 0):03d} ·
{html.escape(ep.get('published', ''))} ·
{html.escape(ep.get('duration_hms', ''))}</p>
{audio_block}
<article>
{body_html}
</article>
<a class="back-link" href="../../">← all episodes</a>
"""
    return render_layout(
        f"{ep.get('title', '')} — {SHOW['title']}",
        article,
        is_root=False,
    )


def render_rss(episodes: list[dict]) -> str:
    now = format_datetime(datetime.now(timezone.utc))
    items = []
    for ep in episodes:
        # Parse the YYYY-MM-DD published date as midnight UTC.
        pub_dt_str = ep.get("published", "")
        try:
            pub_dt = datetime.strptime(pub_dt_str, "%Y-%m-%d").replace(
                tzinfo=timezone.utc
            )
            pub_rfc = format_datetime(pub_dt)
        except ValueError:
            pub_rfc = now

        ep_url = f"{BASE_URL}/episodes/{ep['slug']}/"
        mp3_url = f"{BASE_URL}/episodes/{ep['slug']}/episode.mp3"
        size = ep.get("mp3_size_bytes", 0)
        duration_s = ep.get("duration_seconds", 0)
        hours = duration_s // 3600
        minutes = (duration_s % 3600) // 60
        seconds = duration_s % 60
        if hours:
            itunes_duration = f"{hours:d}:{minutes:02d}:{seconds:02d}"
        else:
            itunes_duration = f"{minutes:d}:{seconds:02d}"

        # Render the post body as HTML for the content:encoded element.
        post_md = ep["_post_path"].read_text(encoding="utf-8")
        post_html = markdown.markdown(
            post_md, extensions=["extra", "smarty", "sane_lists"]
        )

        items.append(f"""    <item>
      <title>{xml_escape(ep.get('title', ''))}</title>
      <link>{xml_escape(ep_url)}</link>
      <guid isPermaLink="false">land-the-plane-{ep.get('number', 0):03d}</guid>
      <pubDate>{pub_rfc}</pubDate>
      <description>{xml_escape(ep.get('summary', ''))}</description>
      <content:encoded><![CDATA[{post_html}]]></content:encoded>
      <enclosure url="{xml_escape(mp3_url)}" length="{size}" type="audio/mpeg"/>
      <itunes:duration>{itunes_duration}</itunes:duration>
      <itunes:explicit>{SHOW['explicit']}</itunes:explicit>
      <itunes:author>{xml_escape(SHOW['author'])}</itunes:author>
      <itunes:subtitle>{xml_escape(ep.get('subtitle', ''))}</itunes:subtitle>
      <itunes:summary>{xml_escape(ep.get('summary', ''))}</itunes:summary>
    </item>""")

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
     xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
     xmlns:content="http://purl.org/rss/1.0/modules/content/"
     xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{xml_escape(SHOW['title'])}</title>
    <link>{xml_escape(BASE_URL)}</link>
    <atom:link href="{xml_escape(BASE_URL)}/feed.xml" rel="self" type="application/rss+xml"/>
    <language>{SHOW['language']}</language>
    <copyright>{xml_escape(SHOW['copyright'])}</copyright>
    <description>{xml_escape(SHOW['description'])}</description>
    <lastBuildDate>{now}</lastBuildDate>
    <itunes:author>{xml_escape(SHOW['author'])}</itunes:author>
    <itunes:summary>{xml_escape(SHOW['description'])}</itunes:summary>
    <itunes:owner>
      <itunes:name>{xml_escape(SHOW['author'])}</itunes:name>
      <itunes:email>{xml_escape(SHOW['email'])}</itunes:email>
    </itunes:owner>
    <itunes:image href="{xml_escape(BASE_URL)}/cover.png"/>
    <itunes:category text="{xml_escape(SHOW['category'])}"/>
    <itunes:explicit>{SHOW['explicit']}</itunes:explicit>
{chr(10).join(items)}
  </channel>
</rss>
"""


def xml_escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
         .replace("<", "&lt;")
         .replace(">", "&gt;")
         .replace('"', "&quot;")
    )


def main() -> int:
    if not EPISODES_DIR.exists():
        print(f"No episodes/ directory at {EPISODES_DIR}", file=sys.stderr)
        return 1

    DOCS_DIR.mkdir(exist_ok=True)
    (DOCS_DIR / "episodes").mkdir(exist_ok=True)
    (DOCS_DIR / "style.css").write_text(STYLE_CSS, encoding="utf-8")

    episodes = discover_episodes()
    print(f"Discovered {len(episodes)} episodes; BASE_URL={BASE_URL}")

    for ep in episodes:
        out_dir = DOCS_DIR / "episodes" / ep["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)

        # Copy the MP3 if it's newer or missing.
        src_mp3 = ep["_mp3_path"]
        dst_mp3 = out_dir / "episode.mp3"
        if not dst_mp3.exists() or src_mp3.stat().st_mtime > dst_mp3.stat().st_mtime:
            shutil.copyfile(src_mp3, dst_mp3)
            print(f"  copied {src_mp3.name} -> {dst_mp3.relative_to(ROOT)}")

        # Render the per-episode page.
        if not ep["_post_path"].exists():
            print(f"  WARN: {ep['slug']} has no post.md; skipping page")
            continue
        page_html = render_episode_page(ep)
        (out_dir / "index.html").write_text(page_html, encoding="utf-8")
        print(f"  wrote {(out_dir / 'index.html').relative_to(ROOT)}")

    (DOCS_DIR / "index.html").write_text(
        render_home(episodes), encoding="utf-8"
    )
    (DOCS_DIR / "feed.xml").write_text(
        render_rss(episodes), encoding="utf-8"
    )
    print(f"Wrote docs/index.html and docs/feed.xml")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
