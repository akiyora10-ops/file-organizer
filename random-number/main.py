import argparse, random
def gen(lo=0, hi=100, n=1):
    return [random.randint(lo,hi) for _ in range(n)]
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("-n", type=int, default=1); p.add_argument("--min", type=int, default=0); p.add_argument("--max", type=int, default=100)
    args=p.parse_args(list(argv) if argv is not None else None)
    for x in gen(args.min, args.max, args.n):
        print(x)
    return 0
if __name__=="__main__":
    raise SystemExit(main())
