"""Apply simple filters to images using Pillow."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageFilter


def apply_filter(src: Path, dst: Path, kind: str) -> None:
    with Image.open(src) as img:
        if kind == "grayscale":
            out = img.convert("L")
        elif kind == "blur":
            out = img.filter(ImageFilter.BLUR)
        elif kind == "sharpen":
            out = img.filter(ImageFilter.SHARPEN)
        elif kind == "edge":
            out = img.filter(ImageFilter.FIND_EDGES)
        elif kind == "contour":
            out = img.filter(ImageFilter.CONTOUR)
        else:
            raise ValueError(f"unknown filter: {kind}")
        out.save(dst)


FILTERS = ["grayscale", "blur", "sharpen", "edge", "contour"]


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Image filters.")
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("-f", "--filter", choices=FILTERS, default="grayscale")
    args = parser.parse_args(list(argv) if argv is not None else None)
    apply_filter(Path(args.input), Path(args.output), args.filter)
    print(f"Applied {args.filter} -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
