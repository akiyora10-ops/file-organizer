import argparse
from pathlib import Path
def find(root):
    return [p for p in Path(root).rglob("*") if p.is_file() and p.stat().st_size==0]
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("path", nargs="?", default=".")
    args=p.parse_args(list(argv) if argv is not None else None)
    for f in find(args.path):
        print(f)
    return 0
if __name__=="__main__":
    raise SystemExit(main())
