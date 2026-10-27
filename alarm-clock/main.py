"""Alarm clock."""

from __future__ import annotations

import argparse, time
from datetime import datetime, timedelta
from typing import Iterable


def seconds_until(target: str) -> float:
    now = datetime.now()
    h, m = (int(x) for x in target.split(":"))
    alarm = now.replace(hour=h, minute=m, second=0, microsecond=0)
    if alarm <= now:
        alarm += timedelta(days=1)
    return (alarm - now).total_seconds()


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Alarm clock.")
    parser.add_argument("time", help="HH:MM")
    parser.add_argument("--demo", action="store_true", help="don't sleep, just compute")
    args = parser.parse_args(list(argv) if argv is not None else None)
    secs = seconds_until(args.time)
    print(f"Alarm in {secs:.0f} seconds")
    if not args.demo:
        time.sleep(min(secs, 0))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
