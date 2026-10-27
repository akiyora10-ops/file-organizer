import argparse
def luhn(number):
    digits=[int(c) for c in number if c.isdigit()]
    total=0
    parity=len(digits)%2
    for i,d in enumerate(digits):
        if i%2==parity:
            d*=2
            if d>9: d-=9
        total+=d
    return total%10==0
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("number")
    args=p.parse_args(list(argv) if argv is not None else None)
    print("valid" if luhn(args.number) else "invalid")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
