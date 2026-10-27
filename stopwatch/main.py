"""Stopwatch utility."""

from __future__ import annotations

import argparse, time
from typing import Iterable


class Stopwatch:
    def __init__(self):
        self.start = None
        self.elapsed = 0.0
        self.running = False

    def start_timer(self):
        if not self.running:
            self.start = time.time() - self.elapsed
            self.running = True

    def stop(self):
        if self.running:
            self.elapsed = time.time() - self.start
            self.running = False

    def reset(self):
        self.elapsed = 0.0
        self.start = None
        self.running = False

    def time(self):
        if self.running:
            return time.time() - self.start
        return self.elapsed


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Stopwatch demo.")
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args(list(argv) if argv is not None else None)
    sw = Stopwatch()
    sw.start_timer()
    time.sleep(0.1)
    sw.stop()
    print(f"Elapsed: {sw.time():.3f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
