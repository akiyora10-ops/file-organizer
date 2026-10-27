import argparse, collections
from pathlib import Path
def freq(text, n=10):
    words=[w.lower().strip(".,!?") for w in text.split()]
    return collections.Counter(words).most_common(n)
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("input", nargs="?"); p.add_argument("-n", type=int, default=10)
    args=p.parse_args(list(argv) if argv is not None else None)
    text=Path(args.input).read_text() if (args.input and Path(args.input).is_file()) else (args.input or "")
    for w,c in freq(text, args.n):
        print(f"{w}: {c}")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
