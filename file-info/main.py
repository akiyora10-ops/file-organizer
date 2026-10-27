import argparse, os
from pathlib import Path
def info(path):
    st=path.stat()
    return {"name":path.name,"size":st.st_size,"modified":st.st_mtime,"is_file":path.is_file()}
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("path")
    args=p.parse_args(list(argv) if argv is not None else None)
    for k,v in info(Path(args.path)).items():
        print(f"{k}: {v}")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
