"""BMI calculator."""

from __future__ import annotations

import argparse
from typing import Iterable


def bmi(weight_kg: float, height_m: float) -> float:
    return weight_kg / (height_m ** 2)


def category(value: float) -> str:
    if value < 18.5:
        return "underweight"
    if value < 25:
        return "normal"
    if value < 30:
        return "overweight"
    return "obese"


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="BMI calculator.")
    parser.add_argument("weight", type=float, help="kg")
    parser.add_argument("height", type=float, help="meters")
    args = parser.parse_args(list(argv) if argv is not None else None)
    value = bmi(args.weight, args.height)
    print(f"BMI: {value:.2f} ({category(value)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
