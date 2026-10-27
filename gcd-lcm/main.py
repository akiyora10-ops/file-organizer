import argparse, math
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("a",type=int); p.add_argument("b",type=int)
    args=p.parse_args(list(argv) if argv is not None else None)
    print("gcd:",math.gcd(args.a,args.b))
    print("lcm:",abs(args.a*args.b)//math.gcd(args.a,args.b))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
