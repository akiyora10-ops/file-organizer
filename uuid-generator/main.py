import uuid, argparse
from typing import Iterable

def gen(n=1, version=4):
    out=[]
    for _ in range(n):
        out.append(str(uuid.uuid4() if version==4 else uuid.uuid1()))
    return out

def main(argv=None):
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("-n", type=int, default=1)
    args=p.parse_args(list(argv) if argv is not None else None)
    for u in gen(args.n):
        print(u)
    return 0

if __name__=="__main__":
    raise SystemExit(main())
