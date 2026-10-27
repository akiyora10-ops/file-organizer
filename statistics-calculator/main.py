import argparse, statistics
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("numbers", nargs="+", type=float)
    args=p.parse_args(list(argv) if argv is not None else None)
    nums=args.numbers
    print("mean:",statistics.mean(nums))
    print("median:",statistics.median(nums))
    print("stdev:",statistics.pstdev(nums))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
