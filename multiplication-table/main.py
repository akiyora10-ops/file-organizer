import argparse
def table(n, limit=10):
    return [[i*j for j in range(1,limit+1)] for i in range(1,n+1)]
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("n", type=int, default=10, nargs="?")
    args=p.parse_args(list(argv) if argv is not None else None)
    for row in table(args.n):
        print(" ".join(f"{x:4}" for x in row))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
