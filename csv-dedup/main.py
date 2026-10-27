import argparse, csv
from pathlib import Path
def dedup(path, column=None):
    seen=set(); out=[]
    with path.open(newline="") as f:
        for r in csv.DictReader(f):
            key=r.get(column) if column else tuple(r.items())
            if key in seen: continue
            seen.add(key); out.append(r)
    return out
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("input"); p.add_argument("-c","--column"); p.add_argument("-o","--output")
    args=p.parse_args(list(argv) if argv is not None else None)
    rows=dedup(Path(args.input), args.column)
    if args.output:
        with Path(args.output).open("w",newline="") as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0].keys()) if rows else []); w.writeheader(); w.writerows(rows)
        print(f"Wrote {len(rows)} rows")
    else:
        for r in rows: print(r)
    return 0
if __name__=="__main__":
    raise SystemExit(main())
