import argparse, csv
from pathlib import Path
def convert(path):
    with path.open(newline="") as f:
        rows=list(csv.reader(f))
    if not rows: return ""
    header=rows[0]; lines=[]
    lines.append("| " + " | ".join(header) + " |")
    lines.append("| " + " | ".join("---" for _ in header) + " |")
    for r in rows[1:]:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("input"); p.add_argument("-o","--output")
    args=p.parse_args(list(argv) if argv is not None else None)
    out=convert(Path(args.input))
    if args.output: Path(args.output).write_text(out); print(f"Wrote {args.output}")
    else: print(out)
    return 0
if __name__=="__main__":
    raise SystemExit(main())
