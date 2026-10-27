"""Generate thumbnails for images in a directory."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

from PIL import Image


def make_thumbnail(src: Path, dst: Path, size: tuple[int, int] = (128, 128)) -> None:
    with Image.open(src) as img:
        img.thumbnail(size)
        dst.parent.mkdir(parents=True, exist_ok=True)
        img.save(dst)


def batch(src_dir: Path, dst_dir: Path, size: tuple[int, int]) -> int:
    dst_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for p in src_dir.iterdir():
        if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif"}:
            make_thumbnail(p, dst_dir / p.name, size)
            count += 1
    return count


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Thumbnail maker.")
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("-s", "--size", default="128x128")
    args = parser.parse_args(list(argv) if argv is not None else None)
    w, h = (int(x) for x in args.size.lower().split("x"))
    src, dst = Path(args.input), Path(args.output)
    if src.is_dir():
        n = batch(src, dst, (w, h))
        print(f"Created {n} thumbnails -> {dst}")
    else:
        make_thumbnail(src, dst, (w, h))
        print(f"Created thumbnail -> {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
