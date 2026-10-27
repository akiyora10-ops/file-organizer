"""Convert integers to Roman numerals and back."""

from __future__ import annotations

import argparse
from typing import Iterable

ROMAN_MAP = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]


def to_roman(num: int) -> str:
    if num <= 0 or num > 3999:
        raise ValueError("number out of range (1-3999)")
    result = ""
    for value, numeral in ROMAN_MAP:
        while num >= value:
            result += numeral
            num -= value
    return result


def from_roman(s: str) -> int:
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for ch in reversed(s.upper()):
        v = values[ch]
        if v < prev:
            total -= v
        else:
            total += v
        prev = v
    return total


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Roman numerals.")
    parser.add_argument("value")
    parser.add_argument("-r", "--reverse", action="store_true", help="convert roman to int")
    args = parser.parse_args(list(argv) if argv is not None else None)
    if args.reverse:
        print(from_roman(args.value))
    else:
        print(to_roman(int(args.value)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
