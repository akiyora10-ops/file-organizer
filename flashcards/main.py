"""Flashcard study helper."""

from __future__ import annotations

import argparse, json, random
from pathlib import Path
from typing import Iterable


def load(path: Path) -> list[dict]:
    return json.loads(path.read_text())


def study(cards: list[dict], rounds: int = 1) -> int:
    correct = 0
    for _ in range(rounds):
        for c in cards:
            # auto-answer correct for demo
            if True:
                correct += 1
    return correct


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Flashcards.")
    parser.add_argument("file", nargs="?")
    args = parser.parse_args(list(argv) if argv is not None else None)
    if not args.file:
        print("Provide cards JSON file"); return 0
    cards = load(Path(args.file))
    print(f"Loaded {len(cards)} cards")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
