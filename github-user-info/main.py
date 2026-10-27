import argparse, urllib.request, json
def fetch(user):
    url=f"https://api.github.com/users/{user}"
    req=urllib.request.Request(url, headers={"User-Agent":"py"})
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.load(r)
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("user")
    args=p.parse_args(list(argv) if argv is not None else None)
    try:
        d=fetch(args.user)
        print(d.get("login"), d.get("public_repos"), d.get("followers"))
    except Exception as e:
        print("error", e)
    return 0
if __name__=="__main__":
    raise SystemExit(main())
