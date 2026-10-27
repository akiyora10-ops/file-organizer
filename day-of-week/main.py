import argparse
from datetime import date
def weekday(d):
    return d.strftime("%A")
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("date", help="YYYY-MM-DD")
    args=p.parse_args(list(argv) if argv is not None else None)
    y,m,dd=map(int,args.date.split("-"))
    print(weekday(date(y,m,dd)))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
