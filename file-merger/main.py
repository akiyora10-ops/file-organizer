"""Concatenate multiple files into one."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable


def merge(inputs: list[Path], output: Path, separator: str = "") -> int:
    total = 0
    with output.open("w", encoding="utf-8") as out:
        for i, inp in enumerate(inputs):
            data = inp.read_text(encoding="utf-8", errors="replace")
            if i and separator:
                out.write(separator)
            out.write(data)
            total += len(data)
    return total


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Merge files.")
    parser.add_argument("inputs", nargs="+")
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("-s", "--separator", default="")
    args = parser.parse_args(list(argv) if argv is not None else None)
    paths = [Path(p) for p in args.inputs]
    n = merge(paths, Path(args.output), args.separator)
    print(f"Merged {len(paths)} files ({n} chars) -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
