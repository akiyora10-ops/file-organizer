import argparse
def is_anagram(a,b):
    return sorted(a.lower().replace(" ",""))==sorted(b.lower().replace(" ",""))
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("a"); p.add_argument("b")
    args=p.parse_args(list(argv) if argv is not None else None)
    print("anagram" if is_anagram(args.a,args.b) else "not anagram")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
