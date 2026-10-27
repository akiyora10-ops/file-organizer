"""Strip HTML tags to plain text."""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path
from typing import Iterable


def strip_tags(text: str) -> str:
    text = re.sub(r"<script[^>]*>.*?</script>", "", text, flags=re.S | re.I)
    text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="HTML to text.")
    parser.add_argument("input", nargs="?")
    parser.add_argument("-o", "--output")
    args = parser.parse_args(list(argv) if argv is not None else None)
    text = Path(args.input).read_text() if (args.input and Path(args.input).is_file()) else (args.input or "")
    out = strip_tags(text)
    if args.output:
        Path(args.output).write_text(out)
        print(f"Wrote {args.output}")
    else:
        print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
