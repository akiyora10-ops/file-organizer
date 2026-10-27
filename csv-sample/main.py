import argparse, csv, random
from pathlib import Path
def sample(path, n=5):
    with path.open(newline="") as f:
        rows=list(csv.DictReader(f))
    return random.sample(rows, min(n,len(rows)))
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("input"); p.add_argument("-n",type=int,default=5); p.add_argument("-s","--seed",type=int)
    args=p.parse_args(list(argv) if argv is not None else None)
    if args.seed is not None: random.seed(args.seed)
    for r in sample(Path(args.input), args.n):
        print(r)
    return 0
if __name__=="__main__":
    raise SystemExit(main())
