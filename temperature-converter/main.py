"""Temperature converter (C/F/K)."""

from __future__ import annotations

import argparse
from typing import Iterable


def convert(value: float, src: str, dst: str) -> float:
    src = src.upper(); dst = dst.upper()
    # to celsius
    if src == "F":
        c = (value - 32) * 5 / 9
    elif src == "K":
        c = value - 273.15
    else:
        c = value
    if dst == "F":
        return c * 9 / 5 + 32
    if dst == "K":
        return c + 273.15
    return c


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Temperature converter.")
    parser.add_argument("value", type=float)
    parser.add_argument("src", choices=["C", "F", "K"])
    parser.add_argument("dst", choices=["C", "F", "K"])
    args = parser.parse_args(list(argv) if argv is not None else None)
    print(round(convert(args.value, args.src, args.dst), 2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
