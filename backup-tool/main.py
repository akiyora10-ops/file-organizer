"""Zip a directory into a backup archive."""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path
from typing import Iterable


def backup(src: Path, dst: Path) -> int:
    count = 0
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in src.rglob("*"):
            if p.is_file():
                zf.write(p, p.relative_to(src))
                count += 1
    return count


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Backup directory to zip.")
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args(list(argv) if argv is not None else None)
    n = backup(Path(args.input), Path(args.output))
    print(f"Backed up {n} files -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
