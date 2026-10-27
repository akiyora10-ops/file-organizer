"""Hangman game logic."""

from __future__ import annotations

import argparse
from typing import Iterable


def mask(word: str, guessed: set[str]) -> str:
    return " ".join(ch if ch.lower() in guessed else "_" for ch in word)


def is_won(word: str, guessed: set[str]) -> bool:
    return all(ch.lower() in guessed or not ch.isalpha() for ch in word)


def is_lost(wrong: int, max_wrong: int = 6) -> bool:
    return wrong >= max_wrong


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Hangman demo.")
    parser.add_argument("word")
    parser.add_argument("guesses", nargs="*")
    args = parser.parse_args(list(argv) if argv is not None else None)
    guessed = set("".join(args.guesses).lower())
    wrong = sum(1 for g in guessed if g not in args.word.lower())
    print(mask(args.word, guessed))
    print("won" if is_won(args.word, guessed) else ("lost" if is_lost(wrong) else "playing"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
