import argparse, http.server, socketserver, os
def serve(directory=".", port=8000):
    os.chdir(directory)
    handler=http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("",port), handler) as httpd:
        print(f"Serving {directory} on port {port}")
        httpd.serve_forever()
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("directory", nargs="?", default="."); p.add_argument("-p","--port", type=int, default=8000)
    args=p.parse_args(list(argv) if argv is not None else None)
    print(f"Would serve {args.directory} on {args.port}")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
