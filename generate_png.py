#!/usr/bin/env python3
"""
generate_percentage_images.py

Generates a sequence of 500x500 PNG images, each showing a percentage
value (0% up to a user-specified maximum), one image per integer percent.

Usage:
    python generate_percentage_images.py --max 100
    python generate_percentage_images.py --max 75 --font "IBMPlexMono-Bold.ttf" --outdir images
    python generate_percentage_images.py --max 100 --bg "#000000" --fg "#00FF00"

Font notes:
    - You can point --font at any .ttf/.otf file on disk.
    - For an "old computer terminal" look, IBM Plex Mono (not Plex Sans) is
      the better pick since it's monospaced -- grab it free from Google Fonts:
      https://fonts.google.com/specimen/IBM+Plex+Mono
      (Plex Sans works too if you prefer a less terminal-like, more modern feel.)
    - If no font is found, the script falls back to Pillow's built-in default
      font, but for the retro-computer aesthetic, you'll want a real font file.
"""

import argparse
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def load_font(font_path: str | None, size: int) -> ImageFont.FreeTypeFont:
    """Try to load the requested font; fall back gracefully if unavailable."""
    candidates = []
    if font_path:
        candidates.append(font_path)

    # A few common fallback locations/names in case the user has Plex
    # installed system-wide or just typed the family name.
    candidates.extend([
        "IBMPlexMono-Regular.ttf",
        "IBMPlexMono-Bold.ttf",
        "/usr/share/fonts/truetype/ibm-plex/IBMPlexMono-Regular.ttf",
        "/System/Library/Fonts/Supplemental/Menlo.ttc",  # macOS mono fallback
        "C:\\Windows\\Fonts\\consola.ttf",  # Windows mono fallback
    ])

    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except (OSError, IOError):
            continue

    print(
        "Warning: could not load a TrueType font "
        f"({font_path!r} or fallbacks). Using Pillow's built-in default font. "
        "Pass --font /path/to/IBMPlexMono-Regular.ttf for the retro look."
    )
    return ImageFont.load_default()


def generate_images(
    max_percent: int,
    outdir: str,
    font_path: str | None,
    bg_color: str,
    fg_color: str,
    width: int = 500,
    height: int = 500,
):
    out_path = Path(outdir)
    out_path.mkdir(parents=True, exist_ok=True)

    # Start large and shrink to fit, since "100%" is wider than "5%".
    font_size = 160
    font = load_font(font_path, font_size)

    digits = len(str(max_percent)) + 1  # +1 for the % sign, rough padding

    for pct in range(0, max_percent + 1):
        text = f"{pct}%"
        img = Image.new("RGB", (width, height), color=bg_color)
        draw = ImageDraw.Draw(img)

        # Recompute font size per-image isn't necessary since we're using
        # one fixed size, but we do want to center the text properly.
        bbox = draw.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]

        x = (width - text_w) / 2 - bbox[0]
        y = (height - text_h) / 2 - bbox[1]

        draw.text((x, y), text, fill=fg_color, font=font)

        filename = out_path / f"{pct:0{digits}d}.png"
        img.save(filename, "PNG")

    print(f"Done. Generated {max_percent + 1} images in '{out_path}/'")


def main():
    parser = argparse.ArgumentParser(
        description="Generate 500x500 PNG images with percentage values 0%% to max%%."
    )
    parser.add_argument(
        "--max", type=int, required=True, help="Maximum percentage value (e.g. 100)"
    )
    parser.add_argument(
        "--outdir", type=str, default="output_images", help="Output directory"
    )
    parser.add_argument(
        "--font",
        type=str,
        default=None,
        help="Path to a .ttf/.otf font file (e.g. IBMPlexMono-Bold.ttf)",
    )
    parser.add_argument(
        "--bg", type=str, default="#FFFFFF", help="Background color (hex or name)"
    )
    parser.add_argument(
        "--fg", type=str, default="#000000", help="Text color (hex or name)"
    )
    args = parser.parse_args()

    if args.max < 0:
        raise SystemExit("--max must be >= 0")

    generate_images(args.max, args.outdir, args.font, args.bg, args.fg)


if __name__ == "__main__":
    main()