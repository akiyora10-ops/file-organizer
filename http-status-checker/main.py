import argparse, urllib.request, urllib.error
def check(url):
    try:
        with urllib.request.urlopen(url, timeout=5) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return None
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("url")
    args=p.parse_args(list(argv) if argv is not None else None)
    print(check(args.url))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
