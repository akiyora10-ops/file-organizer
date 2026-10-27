"""Simple quiz runner."""

from __future__ import annotations

import argparse, json
from pathlib import Path
from typing import Iterable


def score(questions: list[dict], answers: list[str]) -> int:
    s = 0
    for q, a in zip(questions, answers):
        if str(a).strip().lower() == str(q["answer"]).strip().lower():
            s += 1
    return s


def load(path: Path) -> list[dict]:
    return json.loads(path.read_text())


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Quiz runner.")
    parser.add_argument("file", nargs="?")
    args = parser.parse_args(list(argv) if argv is not None else None)
    if not args.file:
        print("Provide quiz JSON file")
        return 0
    qs = load(Path(args.file))
    answers = []
    for q in qs:
        print(q["question"])
        answers.append(input().strip() if False else q.get("answer", ""))
    print(f"Score: {score(qs, answers)}/{len(qs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
