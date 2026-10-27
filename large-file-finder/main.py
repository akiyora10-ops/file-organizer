import argparse
from pathlib import Path
def find(root, min_mb=10):
    threshold=min_mb*1024*1024
    return [p for p in Path(root).rglob("*") if p.is_file() and p.stat().st_size>=threshold]
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("path", nargs="?", default=".")
    p.add_argument("--min-mb", type=int, default=10)
    args=p.parse_args(list(argv) if argv is not None else None)
    for f in find(args.path, args.min_mb):
        print(f)
    return 0
if __name__=="__main__":
    raise SystemExit(main())
