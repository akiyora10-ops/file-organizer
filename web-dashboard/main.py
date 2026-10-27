"""Simple web dashboard serving system info."""

from __future__ import annotations

import argparse, json, platform, http.server, socketserver
from typing import Iterable


def info() -> dict:
    return {
        "platform": platform.platform(),
        "python": platform.python_version(),
        "processor": platform.processor(),
    }


def handler_factory():
    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/api/info":
                data = json.dumps(info()).encode()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(data)
            else:
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(b"<h1>Dashboard</h1>")
        def log_message(self, *a):
            pass
    return H


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Web dashboard.")
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args(list(argv) if argv is not None else None)
    print(json.dumps(info()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
