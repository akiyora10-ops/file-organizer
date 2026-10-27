import argparse
from pathlib import Path
def dump(data, width=16):
    lines=[]
    for i in range(0,len(data),width):
        chunk=data[i:i+width]
        hexpart=" ".join(f"{b:02x}" for b in chunk)
        asciipart="".join(chr(b) if 32<=b<127 else "." for b in chunk)
        lines.append(f"{i:08x}  {hexpart:<{width*3}}  {asciipart}")
    return "\n".join(lines)
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("input")
    args=p.parse_args(list(argv) if argv is not None else None)
    data=Path(args.input).read_bytes()
    print(dump(data))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
