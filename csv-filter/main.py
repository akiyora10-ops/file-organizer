"""Filter CSV rows by column condition."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Iterable


def filter_rows(path: Path, column: str, op: str, value: str) -> list[dict]:
    out = []
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            cell = row.get(column, "")
            ok = False
            if op == "eq":
                ok = cell == value
            elif op == "ne":
                ok = cell != value
            elif op == "contains":
                ok = value in cell
            elif op == "gt":
                try: ok = float(cell) > float(value)
                except ValueError: ok = False
            elif op == "lt":
                try: ok = float(cell) < float(value)
                except ValueError: ok = False
            if ok:
                out.append(row)
    return out


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Filter CSV rows.")
    parser.add_argument("input")
    parser.add_argument("-c", "--column", required=True)
    parser.add_argument("-o", "--op", choices=["eq","ne","contains","gt","lt"], default="eq")
    parser.add_argument("-v", "--value", required=True)
    parser.add_argument("--output")
    args = parser.parse_args(list(argv) if argv is not None else None)
    rows = filter_rows(Path(args.input), args.column, args.op, args.value)
    if args.output:
        import csv as _csv
        with Path(args.output).open("w", newline="", encoding="utf-8") as f:
            w = _csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [])
            w.writeheader()
            for r in rows:
                w.writerow(r)
        print(f"Wrote {len(rows)} rows -> {args.output}")
    else:
        for r in rows:
            print(r)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
