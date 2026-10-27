"""Secure password generator with strength checker."""

from __future__ import annotations

import argparse
import math
import random
import string
from typing import Iterable

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>?/"


def generate(
    length: int = 16,
    use_upper: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    count: int = 1,
) -> list[str]:
    if length < 4:
        raise ValueError("length must be at least 4")
    pools = [LOWER]
    required = [random.choice(LOWER)]
    if use_upper:
        pools.append(UPPER); required.append(random.choice(UPPER))
    if use_digits:
        pools.append(DIGITS); required.append(random.choice(DIGITS))
    if use_symbols:
        pools.append(SYMBOLS); required.append(random.choice(SYMBOLS))
    all_chars = "".join(pools)
    result = []
    for _ in range(count):
        chars = required.copy()
        chars += [random.choice(all_chars) for _ in range(length - len(chars))]
        random.shuffle(chars)
        result.append("".join(chars))
    return result


def entropy_bits(password: str) -> float:
    pool = 0
    if any(c in LOWER for c in password): pool += 26
    if any(c in UPPER for c in password): pool += 26
    if any(c in DIGITS for c in password): pool += 10
    if any(c in SYMBOLS for c in password): pool += len(SYMBOLS)
    if pool == 0:
        return 0.0
    return len(password) * math.log2(pool)


def strength(password: str) -> str:
    bits = entropy_bits(password)
    if bits < 40:
        return "weak"
    if bits < 60:
        return "fair"
    if bits < 80:
        return "strong"
    return "very strong"


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate secure passwords.")
    parser.add_argument("-n", "--length", type=int, default=16)
    parser.add_argument("-c", "--count", type=int, default=1)
    parser.add_argument("--no-upper", action="store_true")
    parser.add_argument("--no-digits", action="store_true")
    parser.add_argument("--no-symbols", action="store_true")
    parser.add_argument("--check", metavar="PASSWORD", help="check strength of a password")
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.check:
        print(f"{args.check}: {strength(args.check)} ({entropy_bits(args.check):.1f} bits)")
        return 0

    for p in generate(
        length=args.length,
        use_upper=not args.no_upper,
        use_digits=not args.no_digits,
        use_symbols=not args.no_symbols,
        count=args.count,
    ):
        print(p)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
