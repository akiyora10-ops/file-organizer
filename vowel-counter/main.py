import argparse
from pathlib import Path
def count(text):
    v=set("aeiouAEIOU")
    return sum(1 for c in text if c in v)
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("input", nargs="?")
    args=p.parse_args(list(argv) if argv is not None else None)
    text=Path(args.input).read_text() if (args.input and Path(args.input).is_file()) else (args.input or "")
    print(count(text))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
