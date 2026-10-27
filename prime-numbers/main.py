"""Prime number utilities: sieve, check, factorization."""

from __future__ import annotations

import argparse
from typing import Iterable


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def sieve(limit: int) -> list[int]:
    if limit < 2:
        return []
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit + 1, i):
                is_p[j] = False
    return [i for i, v in enumerate(is_p) if v]


def factorize(n: int) -> list[int]:
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        factors.append(n)
    return factors


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Prime numbers.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check"); c.add_argument("n", type=int)
    s = sub.add_parser("sieve"); s.add_argument("limit", type=int)
    f = sub.add_parser("factor"); f.add_argument("n", type=int)
    args = parser.parse_args(list(argv) if argv is not None else None)
    if args.cmd == "check":
        print("prime" if is_prime(args.n) else "not prime")
    elif args.cmd == "sieve":
        primes = sieve(args.limit)
        print(len(primes), "primes up to", args.limit)
        print(" ".join(map(str, primes[:50])))
    else:
        print(factorize(args.n))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
