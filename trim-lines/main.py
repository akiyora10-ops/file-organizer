import argparse
from pathlib import Path
def trim(text):
    return "\n".join(line.strip() for line in text.splitlines())
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("input", nargs="?")
    args=p.parse_args(list(argv) if argv is not None else None)
    text=Path(args.input).read_text() if (args.input and Path(args.input).is_file()) else (args.input or "")
    print(trim(text))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
