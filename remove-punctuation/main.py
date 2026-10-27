import argparse, string
from pathlib import Path
def clean(text):
    return text.translate(str.maketrans("","",string.punctuation))
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("input", nargs="?")
    args=p.parse_args(list(argv) if argv is not None else None)
    text=Path(args.input).read_text() if (args.input and Path(args.input).is_file()) else (args.input or "")
    print(clean(text))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
