"""Pretty-print and validate JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable


def format_json(text: str, indent: int = 2, sort_keys: bool = False) -> str:
    obj = json.loads(text)
    return json.dumps(obj, indent=indent, sort_keys=sort_keys, ensure_ascii=False)


def minify(text: str) -> str:
    obj = json.loads(text)
    return json.dumps(obj, separators=(",", ":"), ensure_ascii=False)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Format/validate JSON.")
    parser.add_argument("input", nargs="?")
    parser.add_argument("-o", "--output")
    parser.add_argument("--indent", type=int, default=2)
    parser.add_argument("--sort-keys", action="store_true")
    parser.add_argument("--minify", action="store_true")
    args = parser.parse_args(list(argv) if argv is not None else None)
    text = Path(args.input).read_text() if (args.input and Path(args.input).is_file()) else (args.input or "")
    try:
        out = minify(text) if args.minify else format_json(text, args.indent, args.sort_keys)
    except json.JSONDecodeError as e:
        print(f"invalid JSON: {e}")
        return 1
    if args.output:
        Path(args.output).write_text(out)
        print(f"Wrote {args.output}")
    else:
        print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
