"""Convert between JSON and CSV."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Iterable


def json_to_csv(src: Path, dst: Path) -> int:
    data = json.loads(src.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list) or not data:
        raise ValueError("JSON must be a non-empty array of objects")
    fieldnames = list(data[0].keys())
    for row in data[1:]:
        for k in row:
            if k not in fieldnames:
                fieldnames.append(k)
    with dst.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    return len(data)


def csv_to_json(src: Path, dst: Path) -> int:
    with src.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    dst.write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    return len(rows)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Convert JSON <-> CSV.")
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args(list(argv) if argv is not None else None)
    src, dst = Path(args.input), Path(args.output)
    if src.suffix.lower() == ".json":
        n = json_to_csv(src, dst)
    elif src.suffix.lower() == ".csv":
        n = csv_to_json(src, dst)
    else:
        print("error: input must be .json or .csv")
        return 1
    print(f"Converted {n} record(s) -> {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
