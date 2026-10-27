import argparse, time, hashlib
from pathlib import Path
def file_hash(p):
    h=hashlib.sha256()
    with Path(p).open("rb") as f:
        for c in iter(lambda: f.read(65536), b""): h.update(c)
    return h.hexdigest()
def watch(path, interval=1, iterations=3):
    last=file_hash(path) if Path(path).is_file() else None
    for _ in range(iterations):
        time.sleep(interval)
        if Path(path).is_file():
            cur=file_hash(path)
            if cur!=last:
                print("changed"); last=cur
    return 0
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("path"); p.add_argument("-i","--interval",type=float,default=1); p.add_argument("-n","--iterations",type=int,default=3)
    args=p.parse_args(list(argv) if argv is not None else None)
    watch(args.path, args.interval, args.iterations)
    return 0
if __name__=="__main__":
    raise SystemExit(main())
