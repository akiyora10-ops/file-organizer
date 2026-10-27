"""Number guessing game."""

from __future__ import annotations

import argparse, random
from typing import Iterable


def play(secret: int, guesses: list[int]) -> str:
    for g in guesses:
        if g == secret:
            return "correct"
        if g < secret:
            print("higher")
        else:
            print("lower")
    return "lost"


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Number guessing game.")
    parser.add_argument("--secret", type=int)
    parser.add_argument("--guesses", nargs="*", type=int, default=[])
    args = parser.parse_args(list(argv) if argv is not None else None)
    secret = args.secret if args.secret is not None else random.randint(1, 100)
    if not args.guesses:
        print(f"Secret is {secret} (demo). Run with --guesses to play.")
        return 0
    print(play(secret, args.guesses))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
