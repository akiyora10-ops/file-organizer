import argparse, csv
from pathlib import Path
def convert(path, out):
    with path.open(newline="") as f:
        reader=csv.reader(f, delimiter="\t")
        rows=list(reader)
    with out.open("w",newline="") as f:
        w=csv.writer(f); w.writerows(rows)
    return len(rows)
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("input"); p.add_argument("output")
    args=p.parse_args(list(argv) if argv is not None else None)
    n=convert(Path(args.input), Path(args.output))
    print(f"Converted {n} rows")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
