"""List contents of a zip archive."""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path
from typing import Iterable


def list_zip(path: Path) -> list[tuple[str, int]]:
    with zipfile.ZipFile(path) as zf:
        return [(info.filename, info.file_size) for info in zf.infolist()]


def extract(path: Path, dst: Path) -> int:
    with zipfile.ZipFile(path) as zf:
        zf.extractall(dst)
        return len(zf.namelist())


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Zip lister.")
    parser.add_argument("input")
    parser.add_argument("-x", "--extract", metavar="DIR")
    args = parser.parse_args(list(argv) if argv is not None else None)
    if args.extract:
        n = extract(Path(args.input), Path(args.extract))
        print(f"Extracted {n} entries -> {args.extract}")
    else:
        for name, size in list_zip(Path(args.input)):
            print(f"{size:>8}  {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
