"""Rock paper scissors."""

from __future__ import annotations

import argparse, random
from typing import Iterable

CHOICES = ["rock", "paper", "scissors"]
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def winner(a: str, b: str) -> str:
    a, b = a.lower(), b.lower()
    if a == b:
        return "tie"
    if BEATS[a] == b:
        return "a"
    return "b"


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Rock paper scissors.")
    parser.add_argument("choice", nargs="?", choices=CHOICES)
    args = parser.parse_args(list(argv) if argv is not None else None)
    if not args.choice:
        print("Usage: rps <rock|paper|scissors>")
        return 0
    cpu = random.choice(CHOICES)
    print(f"CPU chose {cpu}")
    w = winner(args.choice, cpu)
    print("You win!" if w == "a" else ("Tie" if w == "tie" else "You lose"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
