import argparse
from pathlib import Path
def rev(text): return text[::-1]
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("input", nargs="?")
    args=p.parse_args(list(argv) if argv is not None else None)
    text=Path(args.input).read_text() if (args.input and Path(args.input).is_file()) else (args.input or "")
    print(rev(text))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
