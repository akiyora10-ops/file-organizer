import argparse, csv
from pathlib import Path
def sort_csv(path, column, reverse=False):
    with path.open(newline="") as f:
        rows=list(csv.DictReader(f)); fieldnames=list(rows[0].keys()) if rows else []
    rows.sort(key=lambda r: r.get(column,""), reverse=reverse)
    return rows, fieldnames
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("input"); p.add_argument("-c","--column",required=True); p.add_argument("-r","--reverse",action="store_true"); p.add_argument("-o","--output")
    args=p.parse_args(list(argv) if argv is not None else None)
    rows,fields=sort_csv(Path(args.input), args.column, args.reverse)
    out=Path(args.output) if args.output else None
    if out:
        with out.open("w",newline="") as f:
            w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
        print(f"Wrote {len(rows)} rows -> {out}")
    else:
        for r in rows: print(r)
    return 0
if __name__=="__main__":
    raise SystemExit(main())
