import argparse, collections
from pathlib import Path
def count(root):
    c=collections.Counter()
    for p in Path(root).rglob("*"):
        if p.is_file():
            c[p.suffix.lower() or "(none)"]+=1
    return c
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("path", nargs="?", default=".")
    args=p.parse_args(list(argv) if argv is not None else None)
    for ext,n in count(args.path).most_common():
        print(f"{ext}: {n}")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
