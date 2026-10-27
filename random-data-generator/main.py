"""Generate random sample data (names, emails, numbers)."""

from __future__ import annotations

import argparse
import random
import string
from typing import Iterable

FIRST = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"]
LAST = ["Smith", "Jones", "Brown", "Taylor", "Wilson", "Davies", "Evans"]


def random_name() -> str:
    return f"{random.choice(FIRST)} {random.choice(LAST)}"


def random_email() -> str:
    user = "".join(random.choice(string.ascii_lowercase) for _ in range(8))
    domain = random.choice(["example.com", "mail.com", "test.org"])
    return f"{user}@{domain}"


def random_phone() -> str:
    return "555-" + "".join(str(random.randint(0, 9)) for _ in range(7))


def generate(n: int, fields: list[str]) -> list[dict]:
    out = []
    for _ in range(n):
        row = {}
        for f in fields:
            if f == "name":
                row[f] = random_name()
            elif f == "email":
                row[f] = random_email()
            elif f == "phone":
                row[f] = random_phone()
            elif f == "age":
                row[f] = random.randint(18, 80)
            elif f == "id":
                row[f] = random.randint(1000, 9999)
        out.append(row)
    return out


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Random data generator.")
    parser.add_argument("-n", type=int, default=5)
    parser.add_argument("-f", "--fields", default="name,email,age")
    parser.add_argument("-o", "--output")
    args = parser.parse_args(list(argv) if argv is not None else None)
    fields = [x.strip() for x in args.fields.split(",")]
    data = generate(args.n, fields)
    import csv
    if args.output:
        with open(args.output, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields)
            w.writeheader()
            w.writerows(data)
        print(f"Wrote {len(data)} rows -> {args.output}")
    else:
        for row in data:
            print(row)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
