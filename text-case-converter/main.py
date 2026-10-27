"""Convert text between cases: upper, lower, title, snake, camel, kebab."""

from __future__ import annotations

import argparse
import re
from typing import Iterable


def to_snake(text: str) -> str:
    text = re.sub(r"[\s-]+", "_", text)
    text = re.sub(r"([A-Z])", r"_\1", text)
    text = re.sub(r"_+", "_", text)
    return text.lower().strip("_")


def to_camel(text: str) -> str:
    parts = re.split(r"[\s_-]+", text)
    return parts[0].lower() + "".join(p.capitalize() for p in parts[1:])


def to_pascal(text: str) -> str:
    parts = re.split(r"[\s_-]+", text)
    return "".join(p.capitalize() for p in parts)


def to_kebab(text: str) -> str:
    return to_snake(text).replace("_", "-")


CONVERTERS = {
    "upper": str.upper,
    "lower": str.lower,
    "title": str.title,
    "snake": to_snake,
    "camel": to_camel,
    "pascal": to_pascal,
    "kebab": to_kebab,
}


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Convert text case.")
    parser.add_argument("text")
    parser.add_argument("-t", "--to", choices=list(CONVERTERS), required=True)
    args = parser.parse_args(list(argv) if argv is not None else None)
    print(CONVERTERS[args.to](args.text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
