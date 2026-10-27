import argparse
from pathlib import Path
def minutes(text, wpm=200):
    words=len(text.split())
    return round(words/wpm,2)
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("input", nargs="?"); p.add_argument("--wpm", type=int, default=200)
    args=p.parse_args(list(argv) if argv is not None else None)
    text=Path(args.input).read_text() if (args.input and Path(args.input).is_file()) else (args.input or "")
    print(f"{minutes(text,args.wpm)} min")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
