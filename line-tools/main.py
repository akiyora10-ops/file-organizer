"""Line-oriented text tools: sort, unique, reverse, shuffle."""

from __future__ import annotations

import argparse
import random
from pathlib import Path
from typing import Iterable


def read_lines(path: Path | None) -> list[str]:
    if path is None:
        import sys
        return sys.stdin.read().splitlines()
    return path.read_text(encoding="utf-8").splitlines()


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Line tools.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sort"); s.add_argument("input", nargs="?"); s.add_argument("-r", "--reverse", action="store_true"); s.add_argument("-u", "--unique", action="store_true")
    u = sub.add_parser("unique"); u.add_argument("input", nargs="?")
    r = sub.add_parser("reverse"); r.add_argument("input", nargs="?")
    sh = sub.add_parser("shuffle"); sh.add_argument("input", nargs="?")
    args = parser.parse_args(list(argv) if argv is not None else None)
    src = Path(args.input) if args.input else None
    lines = read_lines(src)
    if args.cmd == "sort":
        lines = sorted(set(lines) if args.unique else lines, reverse=args.reverse)
    elif args.cmd == "unique":
        seen = set(); out = []
        for l in lines:
            if l not in seen:
                seen.add(l); out.append(l)
        lines = out
    elif args.cmd == "reverse":
        lines = list(reversed(lines))
    elif args.cmd == "shuffle":
        random.shuffle(lines)
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
