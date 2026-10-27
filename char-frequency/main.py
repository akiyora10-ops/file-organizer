import argparse, collections
from pathlib import Path
def freq(text):
    return collections.Counter(text)
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("input", nargs="?")
    args=p.parse_args(list(argv) if argv is not None else None)
    text=Path(args.input).read_text() if (args.input and Path(args.input).is_file()) else (args.input or "")
    for ch,c in freq(text).most_common():
        print(repr(ch), c)
    return 0
if __name__=="__main__":
    raise SystemExit(main())
