"""Convert between Unix timestamps and human-readable dates."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from typing import Iterable


def to_human(ts: int | float, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime(fmt)


def to_timestamp(text: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> int:
    dt = datetime.strptime(text, fmt).replace(tzinfo=timezone.utc)
    return int(dt.timestamp())


def now_ts() -> int:
    return int(datetime.now(tz=timezone.utc).timestamp())


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Timestamp converter.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("to-human"); t.add_argument("ts", type=float)
    u = sub.add_parser("to-ts"); u.add_argument("date", nargs="+")
    n = sub.add_parser("now")
    args = parser.parse_args(list(argv) if argv is not None else None)
    if args.cmd == "to-human":
        print(to_human(args.ts))
    elif args.cmd == "to-ts":
        print(to_timestamp(" ".join(args.date)))
    else:
        print(now_ts())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
