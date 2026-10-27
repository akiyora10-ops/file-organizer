import argparse, socket
def lookup(host):
    return socket.gethostbyname(host)
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("host")
    args=p.parse_args(list(argv) if argv is not None else None)
    try:
        print(lookup(args.host))
    except socket.gaierror as e:
        print("error:", e); return 1
    return 0
if __name__=="__main__":
    raise SystemExit(main())
