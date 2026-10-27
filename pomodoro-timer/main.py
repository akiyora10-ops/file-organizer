"""Pomodoro timer."""

from __future__ import annotations

import argparse, time
from typing import Iterable


def run(work: int, rest: int, cycles: int) -> list[str]:
    phases = []
    for i in range(cycles):
        phases.append(f"work {work}m")
        phases.append(f"rest {rest}m")
    return phases


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Pomodoro timer.")
    parser.add_argument("-w", "--work", type=int, default=25)
    parser.add_argument("-r", "--rest", type=int, default=5)
    parser.add_argument("-c", "--cycles", type=int, default=1)
    args = parser.parse_args(list(argv) if argv is not None else None)
    for phase in run(args.work, args.rest, args.cycles):
        print(phase)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
