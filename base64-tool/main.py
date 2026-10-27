"""Base64 encode/decode text or files."""

from __future__ import annotations

import argparse
import base64
from pathlib import Path
from typing import Iterable


def encode_text(text: str) -> str:
    return base64.b64encode(text.encode()).decode()


def decode_text(text: str) -> str:
    return base64.b64decode(text.encode()).decode()


def encode_file(src: Path, dst: Path | None = None) -> str:
    data = src.read_bytes()
    out = base64.b64encode(data).decode()
    if dst:
        dst.write_text(out)
    return out


def decode_file(src: Path, dst: Path) -> None:
    data = base64.b64decode(src.read_text().encode())
    dst.write_bytes(data)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Base64 encode/decode.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("encode"); e.add_argument("input"); e.add_argument("-o", "--output")
    d = sub.add_parser("decode"); d.add_argument("input"); d.add_argument("-o", "--output")
    f = sub.add_parser("file-encode"); f.add_argument("input"); f.add_argument("output")
    g = sub.add_parser("file-decode"); g.add_argument("input"); g.add_argument("output")
    args = parser.parse_args(list(argv) if argv is not None else None)
    if args.cmd == "encode":
        print(encode_text(args.input if not Path(args.input).exists() else Path(args.input).read_text()))
    elif args.cmd == "decode":
        print(decode_text(args.input if not Path(args.input).exists() else Path(args.input).read_text()))
    elif args.cmd == "file-encode":
        encode_file(Path(args.input), Path(args.output)); print(f"Wrote {args.output}")
    elif args.cmd == "file-decode":
        decode_file(Path(args.input), Path(args.output)); print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
