"""Loan payment calculator."""

from __future__ import annotations

import argparse
from typing import Iterable


def monthly_payment(principal: float, annual_rate: float, months: int) -> float:
    r = annual_rate / 100.0 / 12.0
    if r == 0:
        return principal / months
    return principal * r * (1 + r) ** months / ((1 + r) ** months - 1)


def amortization(principal: float, annual_rate: float, months: int) -> list[dict]:
    r = annual_rate / 100.0 / 12.0
    payment = monthly_payment(principal, annual_rate, months)
    balance = principal
    rows = []
    for i in range(1, months + 1):
        interest = balance * r
        principal_paid = payment - interest
        balance -= principal_paid
        rows.append({"month": i, "payment": round(payment, 2), "principal": round(principal_paid, 2),
                     "interest": round(interest, 2), "balance": round(max(balance, 0), 2)})
    return rows


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Loan calculator.")
    parser.add_argument("principal", type=float)
    parser.add_argument("rate", type=float, help="annual %")
    parser.add_argument("months", type=int)
    parser.add_argument("--schedule", action="store_true")
    args = parser.parse_args(list(argv) if argv is not None else None)
    mp = monthly_payment(args.principal, args.rate, args.months)
    print(f"Monthly payment: {mp:.2f}")
    print(f"Total paid: {mp * args.months:.2f}")
    if args.schedule:
        for row in amortization(args.principal, args.rate, args.months)[:12]:
            print(row)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
