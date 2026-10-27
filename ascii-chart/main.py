"""ASCII bar chart from numbers."""

from __future__ import annotations

import argparse
from typing import Iterable


def chart(values: list[float], width: int = 40) -> str:
    if not values:
        return ""
    mx = max(values)
    lines = []
    for v in values:
        bar_len = int(v / mx * width) if mx else 0
        lines.append("#" * bar_len + f" {v}")
    return "\n".join(lines)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="ASCII bar chart.")
    parser.add_argument("values", nargs="+", type=float)
    parser.add_argument("-w", "--width", type=int, default=40)
    args = parser.parse_args(list(argv) if argv is not None else None)
    print(chart(args.values, args.width))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
