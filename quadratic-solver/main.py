import argparse, cmath
def solve(a,b,c):
    d=b*b-4*a*c
    r1=(-b+cmath.sqrt(d))/(2*a)
    r2=(-b-cmath.sqrt(d))/(2*a)
    return r1,r2
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("a",type=float); p.add_argument("b",type=float); p.add_argument("c",type=float)
    args=p.parse_args(list(argv) if argv is not None else None)
    r1,r2=solve(args.a,args.b,args.c)
    print(r1,r2)
    return 0
if __name__=="__main__":
    raise SystemExit(main())
