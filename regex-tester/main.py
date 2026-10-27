"""Test a regex against input text or file."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Iterable


def find_matches(pattern: str, text: str, flags: int = 0) -> list[re.Match]:
    return list(re.finditer(pattern, text, flags))


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Regex tester.")
    parser.add_argument("pattern")
    parser.add_argument("input", nargs="?")
    parser.add_argument("-f", "--file", action="store_true")
    parser.add_argument("-i", "--ignore-case", action="store_true")
    parser.add_argument("-g", "--group", type=int, default=0)
    args = parser.parse_args(list(argv) if argv is not None else None)
    text = Path(args.input).read_text() if (args.file or (args.input and Path(args.input).is_file())) else (args.input or "")
    flags = re.IGNORECASE if args.ignore_case else 0
    try:
        matches = find_matches(args.pattern, text, flags)
    except re.error as e:
        print(f"regex error: {e}")
        return 1
    print(f"{len(matches)} match(es)")
    for m in matches:
        print(f"  [{m.start()}:{m.end()}] {m.group(args.group)!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
