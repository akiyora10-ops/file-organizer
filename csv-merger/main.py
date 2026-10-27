"""Merge multiple CSV files into one (same headers)."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Iterable


def merge(inputs: list[Path], output: Path) -> int:
    rows_written = 0
    fieldnames = None
    with output.open("w", newline="", encoding="utf-8") as outf:
        writer = None
        for inp in inputs:
            with inp.open(newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                if fieldnames is None:
                    fieldnames = reader.fieldnames
                    writer = csv.DictWriter(outf, fieldnames=fieldnames)
                    writer.writeheader()
                for row in reader:
                    writer.writerow(row)
                    rows_written += 1
    return rows_written


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Merge CSV files.")
    parser.add_argument("inputs", nargs="+")
    parser.add_argument("-o", "--output", required=True)
    args = parser.parse_args(list(argv) if argv is not None else None)
    paths = [Path(p) for p in args.inputs]
    n = merge(paths, Path(args.output))
    print(f"Merged {len(paths)} files -> {n} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
