import argparse
from pathlib import Path
def tail(path, n=10):
    lines=path.read_text().splitlines()
    return lines[-n:]
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("input"); p.add_argument("-n", type=int, default=10)
    args=p.parse_args(list(argv) if argv is not None else None)
    for l in tail(Path(args.input), args.n):
        print(l)
    return 0
if __name__=="__main__":
    raise SystemExit(main())
