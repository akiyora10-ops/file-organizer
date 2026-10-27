"""Resize and convert images using Pillow."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

from PIL import Image


def resize_image(src: Path, dst: Path, width: int | None = None, height: int | None = None, quality: int = 85) -> None:
    with Image.open(src) as img:
        if width or height:
            w = width or img.width
            h = height or int(img.height * (w / img.width))
            if not width:
                w = int(img.width * (h / img.height))
            img = img.resize((w, h), Image.LANCZOS)
        out_format = dst.suffix.lstrip(".").upper() or img.format
        if out_format == "JPG":
            out_format = "JPEG"
        img.save(dst, format=out_format, quality=quality)


def batch_resize(src_dir: Path, dst_dir: Path, width: int | None = None, height: int | None = None) -> int:
    dst_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for p in src_dir.iterdir():
        if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif"}:
            resize_image(p, dst_dir / p.name, width=width, height=height)
            count += 1
    return count


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Resize images.")
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--width", type=int)
    parser.add_argument("--height", type=int)
    parser.add_argument("--quality", type=int, default=85)
    args = parser.parse_args(list(argv) if argv is not None else None)
    src, dst = Path(args.input), Path(args.output)
    if src.is_dir():
        n = batch_resize(src, dst, width=args.width, height=args.height)
        print(f"Resized {n} image(s) -> {dst}")
    else:
        resize_image(src, dst, width=args.width, height=args.height, quality=args.quality)
        print(f"Resized -> {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
