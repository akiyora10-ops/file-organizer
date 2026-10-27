import argparse, socket
def info(host):
    ip=socket.gethostbyname(host)
    return {"host":host,"ip":ip}
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("host", nargs="?", default="localhost")
    args=p.parse_args(list(argv) if argv is not None else None)
    print(info(args.host))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
