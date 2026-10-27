"""Generate URL-friendly slugs from text."""

from __future__ import annotations

import argparse
import re
import unicodedata
from typing import Iterable


def slugify(text: str, separator: str = "-") -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", separator, text)
    text = text.strip(separator)
    text = re.sub(rf"{re.escape(separator)}+", separator, text)
    return text


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Slug generator.")
    parser.add_argument("text", nargs="+")
    parser.add_argument("-s", "--separator", default="-")
    args = parser.parse_args(list(argv) if argv is not None else None)
    print(slugify(" ".join(args.text), args.separator))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
