"""Convert numbers between bases (2-36)."""

from __future__ import annotations

import argparse
from typing import Iterable


def to_base(n: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("base must be 2-36")
    if n == 0:
        return "0"
    neg = n < 0
    n = abs(n)
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = ""
    while n:
        out = digits[n % base] + out
        n //= base
    return ("-" if neg else "") + out


def from_base(s: str, base: int) -> int:
    return int(s, base)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Base converter.")
    parser.add_argument("value")
    parser.add_argument("-f", "--from-base", type=int, default=10)
    parser.add_argument("-t", "--to-base", type=int, default=2)
    args = parser.parse_args(list(argv) if argv is not None else None)
    n = from_base(args.value, args.from_base)
    print(to_base(n, args.to_base))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
