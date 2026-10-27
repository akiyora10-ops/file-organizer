"""Caesar cipher encrypt/decrypt."""

from __future__ import annotations

import argparse
from typing import Iterable


def shift(text: str, k: int) -> str:
    out = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            out.append(chr((ord(ch) - base + k) % 26 + base))
        else:
            out.append(ch)
    return "".join(out)


def encrypt(text: str, k: int) -> str:
    return shift(text, k)


def decrypt(text: str, k: int) -> str:
    return shift(text, -k)


def brute_force(text: str) -> list[str]:
    return [f"{i}: {shift(text, -i)}" for i in range(26)]


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Caesar cipher.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("encrypt"); e.add_argument("text", nargs="+"); e.add_argument("-k", type=int, default=3)
    d = sub.add_parser("decrypt"); d.add_argument("text", nargs="+"); d.add_argument("-k", type=int, default=3)
    b = sub.add_parser("brute"); b.add_argument("text", nargs="+")
    args = parser.parse_args(list(argv) if argv is not None else None)
    text = " ".join(args.text)
    if args.cmd == "encrypt":
        print(encrypt(text, args.k))
    elif args.cmd == "decrypt":
        print(decrypt(text, args.k))
    else:
        print("\n".join(brute_force(text)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
