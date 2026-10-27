import argparse, re
def is_palindrome(text):
    t=re.sub(r"[^a-z0-9]","",text.lower())
    return t==t[::-1]
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("text", nargs="+")
    args=p.parse_args(list(argv) if argv is not None else None)
    print("palindrome" if is_palindrome(" ".join(args.text)) else "not palindrome")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
