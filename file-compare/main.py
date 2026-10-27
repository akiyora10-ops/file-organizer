"""Compare two text files and show differences."""

from __future__ import annotations

import argparse
import difflib
from pathlib import Path
from typing import Iterable


def compare(a: Path, b: Path) -> str:
    la = a.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
    lb = b.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
    diff = difflib.unified_diff(la, lb, fromfile=str(a), tofile=str(b))
    return "".join(diff)


def similarity(a: Path, b: Path) -> float:
    la = a.read_text(encoding="utf-8", errors="replace").splitlines()
    lb = b.read_text(encoding="utf-8", errors="replace").splitlines()
    return difflib.SequenceMatcher(None, la, lb).ratio()


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Compare files.")
    parser.add_argument("a")
    parser.add_argument("b")
    parser.add_argument("--ratio", action="store_true")
    args = parser.parse_args(list(argv) if argv is not None else None)
    pa, pb = Path(args.a), Path(args.b)
    if args.ratio:
        print(f"{similarity(pa, pb):.2%}")
    else:
        out = compare(pa, pb)
        print(out if out else "Files are identical.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
