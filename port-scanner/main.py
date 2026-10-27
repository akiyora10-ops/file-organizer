import argparse, socket
from typing import Iterable
def scan(host, ports):
    open_ports=[]
    for p in ports:
        s=socket.socket(); s.settimeout(0.5)
        try:
            if s.connect_ex((host,p))==0: open_ports.append(p)
        finally: s.close()
    return open_ports
def parse_ports(spec):
    if "-" in spec:
        a,b=spec.split("-"); return list(range(int(a),int(b)+1))
    return [int(x) for x in spec.split(",")]
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("host"); p.add_argument("-p","--ports",default="1-1024")
    args=p.parse_args(list(argv) if argv is not None else None)
    ports=parse_ports(args.ports)
    print("Open:", scan(args.host, ports))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
