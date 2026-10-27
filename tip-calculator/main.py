"""Tip and bill splitter."""

from __future__ import annotations

import argparse
from typing import Iterable


def calculate(bill: float, tip_percent: float, people: int = 1) -> dict:
    tip = bill * tip_percent / 100.0
    total = bill + tip
    return {
        "bill": round(bill, 2),
        "tip": round(tip, 2),
        "total": round(total, 2),
        "per_person": round(total / people, 2),
    }


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Tip calculator.")
    parser.add_argument("bill", type=float)
    parser.add_argument("-t", "--tip", type=float, default=15.0)
    parser.add_argument("-p", "--people", type=int, default=1)
    args = parser.parse_args(list(argv) if argv is not None else None)
    r = calculate(args.bill, args.tip, args.people)
    for k, v in r.items():
        print(f"{k}: {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
