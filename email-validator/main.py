import re, argparse
from typing import Iterable
PAT=re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
def is_valid(email): return bool(PAT.match(email))
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("email")
    args=p.parse_args(list(argv) if argv is not None else None)
    print("valid" if is_valid(args.email) else "invalid")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
