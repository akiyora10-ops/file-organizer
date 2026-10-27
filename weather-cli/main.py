import argparse, urllib.request, json
def fetch(lat, lon):
    url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    with urllib.request.urlopen(url, timeout=10) as r:
        data=json.load(r)
    return data.get("current_weather",{})
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("--lat", type=float, default=51.5); p.add_argument("--lon", type=float, default=-0.12)
    args=p.parse_args(list(argv) if argv is not None else None)
    w=fetch(args.lat, args.lon)
    print(w)
    return 0
if __name__=="__main__":
    raise SystemExit(main())
