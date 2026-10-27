"""URL encode/decode strings."""

from __future__ import annotations

import argparse
import urllib.parse
from typing import Iterable


def encode(text: str) -> str:
    return urllib.parse.quote(text)


def decode(text: str) -> str:
    return urllib.parse.unquote(text)


def encode_qs(params: dict) -> str:
    return urllib.parse.urlencode(params)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="URL encode/decode.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("encode"); e.add_argument("text", nargs="+")
    d = sub.add_parser("decode"); d.add_argument("text", nargs="+")
    args = parser.parse_args(list(argv) if argv is not None else None)
    text = " ".join(args.text)
    if args.cmd == "encode":
        print(encode(text))
    else:
        print(decode(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
