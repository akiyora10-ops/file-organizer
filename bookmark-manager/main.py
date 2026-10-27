"""bookmark-manager manager (SQLite)."""

from __future__ import annotations
import argparse, sqlite3
from pathlib import Path
from typing import Iterable

DB = Path("data.db")

def connect(db=DB):
    conn = sqlite3.connect(str(db))
    conn.execute("""CREATE TABLE IF NOT EXISTS bookmarks (id INTEGER PRIMARY KEY, title TEXT, url TEXT)""")
    conn.commit()
    return conn

def add(values, db=DB):
    conn = connect(db)
    placeholders = ",".join("?" for _ in values)
    cur = conn.execute("INSERT INTO bookmarks (title,url) VALUES (" + placeholders + ")", values)
    conn.commit()
    tid = cur.lastrowid
    conn.close()
    return tid

def list_all(db=DB):
    conn = connect(db)
    rows = conn.execute("SELECT * FROM bookmarks").fetchall()
    conn.close()
    return rows

def search(term, db=DB):
    conn = connect(db)
    rows = conn.execute("SELECT * FROM bookmarks WHERE " + " OR ".join(f"{f} LIKE ?" for f in fields), [f"%{term}%"]*len(fields)).fetchall()
    conn.close()
    return rows

def delete(tid, db=DB):
    conn = connect(db)
    cur = conn.execute("DELETE FROM bookmarks WHERE id=?", (tid,))
    conn.commit()
    ok = cur.rowcount > 0
    conn.close()
    return ok

def main(argv=None):
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add"); 
    for f in fields:
        a.add_argument("--"+f.replace("_","-"))
    l = sub.add_parser("list")
    s = sub.add_parser("search"); s.add_argument("term")
    d = sub.add_parser("delete"); d.add_argument("id", type=int)
    args = p.parse_args(list(argv) if argv is not None else None)
    if args.cmd == "add":
        vals = [getattr(args, f) for f in fields]
        print("Added #"+str(add(vals, db=Path("test.db") if False else DB)))
    elif args.cmd == "list":
        for r in list_all():
            print(r)
    elif args.cmd == "search":
        for r in search(args.term):
            print(r)
    else:
        print("Deleted." if delete(args.id) else "Not found.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
