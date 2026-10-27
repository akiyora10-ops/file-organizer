"""Convert text to ASCII art using built-in font."""

from __future__ import annotations

import argparse
from typing import Iterable

FONT = {
    "A": ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
    "B": ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "],
    "C": [" CCC ", "C   C", "C    ", "C   C", " CCC "],
}
DEFAULT = ["?"] * 5


def render(text: str) -> str:
    lines = [""] * 5
    for ch in text.upper():
        glyph = FONT.get(ch, DEFAULT)
        for i in range(5):
            lines[i] += glyph[i] + " "
    return "\n".join(lines)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="ASCII art text.")
    parser.add_argument("text", nargs="+")
    args = parser.parse_args(list(argv) if argv is not None else None)
    print(render(" ".join(args.text)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
