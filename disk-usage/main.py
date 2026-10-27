"""Show disk usage of directories."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable


def dir_size(path: Path) -> int:
    total = 0
    for p in path.rglob("*"):
        if p.is_file():
            try:
                total += p.stat().st_size
            except OSError:
                pass
    return total


def top_dirs(root: Path, n: int = 10) -> list[tuple[Path, int]]:
    results = []
    for child in root.iterdir():
        if child.is_dir():
            results.append((child, dir_size(child)))
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:n]


def human(size: int) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} PB"


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Disk usage.")
    parser.add_argument("path", nargs="?", default=".")
    parser.add_argument("-n", type=int, default=10)
    args = parser.parse_args(list(argv) if argv is not None else None)
    root = Path(args.path)
    print(f"{human(dir_size(root))}  {root}")
    for child, size in top_dirs(root, args.n):
        print(f"{human(size):>10}  {child}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
