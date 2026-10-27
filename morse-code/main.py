"""Encode/decode Morse code."""

from __future__ import annotations

import argparse
from typing import Iterable

MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", ".": ".-.-.-", ",": "--..--", "?": "..--..",
    " ": "/",
}
REVERSE = {v: k for k, v in MORSE.items()}


def encode(text: str) -> str:
    return " ".join(MORSE.get(ch.upper(), "") for ch in text)


def decode(text: str) -> str:
    return "".join(REVERSE.get(tok, "") for tok in text.split(" "))


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Morse code.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("encode"); e.add_argument("text", nargs="+")
    d = sub.add_parser("decode"); d.add_argument("code", nargs="+")
    args = parser.parse_args(list(argv) if argv is not None else None)
    if args.cmd == "encode":
        print(encode(" ".join(args.text)))
    else:
        print(decode(" ".join(args.code)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
