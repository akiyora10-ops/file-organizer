import argparse, random, string
def gen(n=10, charset=string.ascii_letters+string.digits):
    return "".join(random.choice(charset) for _ in range(n))
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("-n", type=int, default=10)
    args=p.parse_args(list(argv) if argv is not None else None)
    print(gen(args.n))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
