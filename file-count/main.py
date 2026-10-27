import argparse
from pathlib import Path
def count(root):
    files=[p for p in Path(root).rglob("*") if p.is_file()]
    dirs=[p for p in Path(root).rglob("*") if p.is_dir()]
    return len(files), len(dirs)
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("path", nargs="?", default=".")
    args=p.parse_args(list(argv) if argv is not None else None)
    f,d=count(args.path)
    print(f"files: {f}, dirs: {d}")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
