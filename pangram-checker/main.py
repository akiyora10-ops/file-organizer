import argparse, string
def is_pangram(text):
    return set(string.ascii_lowercase) <= set(text.lower())
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("text", nargs="+")
    args=p.parse_args(list(argv) if argv is not None else None)
    print("pangram" if is_pangram(" ".join(args.text)) else "not pangram")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
