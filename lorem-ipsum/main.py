"""Generate lorem ipsum placeholder text."""

from __future__ import annotations

import argparse
import random
from typing import Iterable

WORDS = ("lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing",
         "elit", "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore",
         "et", "dolore", "magna", "aliqua")


def sentence(words: int = 8) -> str:
    return " ".join(random.choice(WORDS) for _ in range(words)).capitalize() + "."


def paragraph(sentences: int = 5) -> str:
    return " ".join(sentence() for _ in range(sentences))


def generate(paragraphs: int = 1, sentences: int = 5, words: int = 8) -> str:
    return "\n\n".join(paragraph(sentences) for _ in range(paragraphs))


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lorem ipsum generator.")
    parser.add_argument("-p", "--paragraphs", type=int, default=1)
    parser.add_argument("-s", "--sentences", type=int, default=5)
    parser.add_argument("-w", "--words", type=int, default=8)
    parser.add_argument("-o", "--output")
    args = parser.parse_args(list(argv) if argv is not None else None)
    text = generate(args.paragraphs, args.sentences, args.words)
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(text)
        print(f"Wrote {args.output}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
