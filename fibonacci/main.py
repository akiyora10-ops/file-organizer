"""Fibonacci sequence generator."""

from __future__ import annotations

import argparse
from typing import Iterable


def fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Fibonacci.")
    parser.add_argument("n", type=int)
    parser.add_argument("--nth", action="store_true", help="print nth value only")
    args = parser.parse_args(list(argv) if argv is not None else None)
    if args.nth:
        print(fib(args.n))
    else:
        print(" ".join(map(str, fibonacci(args.n))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
