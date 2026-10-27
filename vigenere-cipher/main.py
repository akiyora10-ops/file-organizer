"""Vigenere cipher encrypt/decrypt."""

from __future__ import annotations

import argparse
from typing import Iterable


def _shift_char(ch: str, k: int) -> str:
    if ch.isalpha():
        base = ord("A") if ch.isupper() else ord("a")
        return chr((ord(ch) - base + k) % 26 + base)
    return ch


def encrypt(text: str, key: str) -> str:
    out = []; ki = 0
    for ch in text:
        if ch.isalpha():
            k = ord(key[ki % len(key)].upper()) - ord("A")
            out.append(_shift_char(ch, k)); ki += 1
        else:
            out.append(ch)
    return "".join(out)


def decrypt(text: str, key: str) -> str:
    out = []; ki = 0
    for ch in text:
        if ch.isalpha():
            k = ord(key[ki % len(key)].upper()) - ord("A")
            out.append(_shift_char(ch, -k)); ki += 1
        else:
            out.append(ch)
    return "".join(out)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Vigenere cipher.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("encrypt"); e.add_argument("text", nargs="+"); e.add_argument("-k", "--key", required=True)
    d = sub.add_parser("decrypt"); d.add_argument("text", nargs="+"); d.add_argument("-k", "--key", required=True)
    args = parser.parse_args(list(argv) if argv is not None else None)
    text = " ".join(args.text)
    if args.cmd == "encrypt":
        print(encrypt(text, args.key))
    else:
        print(decrypt(text, args.key))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
