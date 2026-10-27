import argparse, json
from pathlib import Path
def flatten(obj, prefix=""):
    out={}
    if isinstance(obj, dict):
        for k,v in obj.items():
            out.update(flatten(v, f"{prefix}.{k}" if prefix else k))
    elif isinstance(obj, list):
        for i,v in enumerate(obj):
            out.update(flatten(v, f"{prefix}[{i}]"))
    else:
        out[prefix]=obj
    return out
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("input", nargs="?")
    args=p.parse_args(list(argv) if argv is not None else None)
    text=Path(args.input).read_text() if (args.input and Path(args.input).is_file()) else (args.input or "")
    print(json.dumps(flatten(json.loads(text)), indent=2))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
