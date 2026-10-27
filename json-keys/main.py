import argparse, json
from pathlib import Path
def keys(obj, prefix=""):
    out=[]
    if isinstance(obj, dict):
        for k,v in obj.items():
            out.append((prefix+"."+k) if prefix else k)
            out.extend(keys(v, (prefix+"."+k) if prefix else k))
    elif isinstance(obj, list):
        for i,v in enumerate(obj):
            out.extend(keys(v, f"{prefix}[{i}]"))
    return out
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("input", nargs="?")
    args=p.parse_args(list(argv) if argv is not None else None)
    text=Path(args.input).read_text() if (args.input and Path(args.input).is_file()) else (args.input or "")
    for k in keys(json.loads(text)):
        print(k)
    return 0
if __name__=="__main__":
    raise SystemExit(main())
