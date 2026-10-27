"""Countdown timer CLI."""

from __future__ import annotations

import argparse
import re
import sys
import time
from typing import Iterable


def parse_duration(text: str) -> int:
    text = text.strip().lower()
    if text.isdigit():
        return int(text)
    m = re.fullmatch(r"(\d+)\s*(s|sec|seconds|m|min|minutes|h|hr|hours)", text)
    if not m:
        raise ValueError(f"invalid duration: {text}")
    value = int(m.group(1))
    unit = m.group(2)
    if unit.startswith("s"):
        return value
    if unit.startswith("m"):
        return value * 60
    return value * 3600


def format_remaining(seconds: int) -> str:
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


def countdown(seconds: int, message: str = "", tick: float = 1.0) -> None:
    remaining = seconds
    while remaining >= 0:
        sys.stdout.write(f"\r{format_remaining(remaining)} {message}".rstrip() + "  ")
        sys.stdout.flush()
        if remaining == 0:
            break
        time.sleep(tick)
        remaining -= 1
    sys.stdout.write("\n")
    print("Time's up!")


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Countdown timer.")
    parser.add_argument("duration", help="e.g. 30, 5m, 1h")
    parser.add_argument("-m", "--message", default="")
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        seconds = parse_duration(args.duration)
    except ValueError as e:
        print(f"error: {e}")
        return 1
    countdown(seconds, message=args.message, tick=0.0 if seconds == 0 else 1.0)
    # avoid sleeping in tests? tick param controls; default 1.0 for real run
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
