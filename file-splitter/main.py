"""Split a file into chunks by lines or bytes."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable


def split_lines(src: Path, lines_per: int, out_prefix: Path) -> int:
    count = 0
    chunk: list[str] = []
    idx = 0
    with src.open(encoding="utf-8", errors="replace") as f:
        for line in f:
            chunk.append(line)
            if len(chunk) >= lines_per:
                (out_prefix.parent / f"{out_prefix.name}_{idx:03d}.txt").write_text("".join(chunk))
                chunk = []; idx += 1; count += 1
        if chunk:
            (out_prefix.parent / f"{out_prefix.name}_{idx:03d}.txt").write_text("".join(chunk))
            count += 1
    return count


def split_bytes(src: Path, bytes_per: int, out_prefix: Path) -> int:
    idx = 0; count = 0
    with src.open("rb") as f:
        while True:
            data = f.read(bytes_per)
            if not data:
                break
            (out_prefix.parent / f"{out_prefix.name}_{idx:03d}.bin").write_bytes(data)
            idx += 1; count += 1
    return count


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Split a file.")
    parser.add_argument("input")
    parser.add_argument("-n", "--lines", type=int, default=0)
    parser.add_argument("-b", "--bytes", type=int, default=0)
    parser.add_argument("-o", "--output", default="chunk")
    args = parser.parse_args(list(argv) if argv is not None else None)
    src = Path(args.input)
    prefix = Path(args.output)
    prefix.parent.mkdir(parents=True, exist_ok=True)
    if args.bytes:
        n = split_bytes(src, args.bytes, prefix)
    else:
        n = split_lines(src, args.lines or 100, prefix)
    print(f"Split into {n} chunk(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
