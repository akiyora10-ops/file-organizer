"""Age calculator from birthdate."""

from __future__ import annotations

import argparse
from datetime import date, datetime
from typing import Iterable


def age(birth: date, today: date | None = None) -> tuple[int, int, int]:
    today = today or date.today()
    years = today.year - birth.year
    if (today.month, today.day) < (birth.month, birth.day):
        years -= 1
    # months/days approx
    months = (today.year - birth.year) * 12 + (today.month - birth.month)
    if today.day < birth.day:
        months -= 1
    days = (today - birth).days
    return years, months, days


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Age calculator.")
    parser.add_argument("birthdate", help="YYYY-MM-DD")
    args = parser.parse_args(list(argv) if argv is not None else None)
    b = datetime.strptime(args.birthdate, "%Y-%m-%d").date()
    y, m, d = age(b)
    print(f"{y} years, {m} months, {d} days")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
