"""Print directory tree."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable


def tree(root: Path, max_depth: int = 4, prefix: str = "") -> list[str]:
    lines = [str(root)]
    if max_depth <= 0 or not root.is_dir():
        return lines
    entries = sorted(root.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    for i, entry in enumerate(entries):
        connector = "└── " if i == len(entries) - 1 else "├── "
        lines.append(prefix + connector + entry.name)
        if entry.is_dir():
            ext = "    " if i == len(entries) - 1 else "│   "
            lines.extend(tree(entry, max_depth - 1, prefix + ext)[1:])
    return lines


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Directory tree.")
    parser.add_argument("path", nargs="?", default=".")
    parser.add_argument("-d", "--depth", type=int, default=4)
    args = parser.parse_args(list(argv) if argv is not None else None)
    root = Path(args.path)
    print("\n".join(tree(root, args.depth)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
