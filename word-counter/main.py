"""Count words, lines, characters, and sentences in text."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
from typing import Iterable


def stats(text: str) -> dict:
    words = text.split()
    sentences = [s for s in text.replace("!", ".").replace("?", ".").split(".") if s.strip()]
    return {
        "lines": text.count("\n") + (1 if text and not text.endswith("\n") else 0),
        "words": len(words),
        "chars": len(text),
        "chars_no_space": len(text.replace(" ", "").replace("\n", "")),
        "sentences": len(sentences),
        "unique_words": len(set(w.lower().strip(".,!?") for w in words)),
    }


def top_words(text: str, n: int = 10) -> list[tuple[str, int]]:
    words = [w.lower().strip(".,!?") for w in text.split()]
    return Counter(words).most_common(n)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Word counter.")
    parser.add_argument("input", nargs="?")
    parser.add_argument("-t", "--top", type=int, default=0)
    args = parser.parse_args(list(argv) if argv is not None else None)
    if args.input and Path(args.input).exists():
        text = Path(args.input).read_text(encoding="utf-8", errors="replace")
    else:
        text = args.input or ""
    s = stats(text)
    for k, v in s.items():
        print(f"{k}: {v}")
    if args.top:
        print("top words:")
        for w, c in top_words(text, args.top):
            print(f"  {w}: {c}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
