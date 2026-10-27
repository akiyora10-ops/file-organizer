"""Hash text or files (md5, sha1, sha256, sha512)."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from typing import Iterable

ALGOS = ("md5", "sha1", "sha256", "sha512")


def hash_text(text: str, algo: str = "sha256") -> str:
    h = hashlib.new(algo)
    h.update(text.encode())
    return h.hexdigest()


def hash_file(path: Path, algo: str = "sha256", chunk: int = 65536) -> str:
    h = hashlib.new(algo)
    with path.open("rb") as f:
        for block in iter(lambda: f.read(chunk), b""):
            h.update(block)
    return h.hexdigest()


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Hash text or files.")
    parser.add_argument("input")
    parser.add_argument("-a", "--algo", choices=ALGOS, default="sha256")
    parser.add_argument("-f", "--file", action="store_true", help="treat input as file path")
    args = parser.parse_args(list(argv) if argv is not None else None)
    if args.file:
        print(hash_file(Path(args.input), args.algo))
    else:
        p = Path(args.input)
        if p.exists() and p.is_file():
            print(hash_file(p, args.algo))
        else:
            print(hash_text(args.input, args.algo))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
