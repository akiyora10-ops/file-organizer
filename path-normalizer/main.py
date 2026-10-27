import argparse, os
from pathlib import Path
def normalize(p):
    return str(Path(p).resolve())
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("path")
    args=p.parse_args(list(argv) if argv is not None else None)
    print(normalize(args.path))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
