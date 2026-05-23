#!/usr/bin/env python3
"""Generate a simple podcast cover image.

Apple Podcasts wants 1400x1400 to 3000x3000 JPG/PNG, RGB, sRGB. This
script writes a 1400x1400 PNG to docs/cover.png. Replace it with a real
piece of cover art whenever you have one — anywhere that file exists,
build_site.py will pick it up.
"""
from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent.parent / "docs" / "cover.png"
SIZE = 1400


def find_font(size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
    ]
    for p in candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)

    img = Image.new("RGB", (SIZE, SIZE), (10, 14, 24))
    draw = ImageDraw.Draw(img)

    # Soft radial-ish gradient corner accent
    for r in range(800, 0, -8):
        alpha = int(60 * (r / 800))
        draw.ellipse(
            (-r + 200, -r + 200, r + 200, r + 200),
            fill=(120 - alpha // 3, 60 + alpha // 4, 200 - alpha // 2),
        )

    title = "claude\ncast"
    subtitle = "engineering in the agentic era"

    title_font = find_font(360)
    sub_font = find_font(56)

    # Title
    draw.multiline_text(
        (110, 360),
        title,
        font=title_font,
        fill=(240, 240, 250),
        spacing=20,
    )

    # Subtitle
    draw.text(
        (114, 1240),
        subtitle,
        font=sub_font,
        fill=(180, 180, 200),
    )

    # A thin underline accent
    draw.rectangle((114, 1320, 480, 1330), fill=(200, 120, 255))

    img.save(OUT, "PNG", optimize=True)
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
