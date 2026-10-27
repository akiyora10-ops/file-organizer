"""Simple SQLite-backed todo CLI."""

from __future__ import annotations

import argparse
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Iterable

DB_PATH = Path.home() / ".todo_cli.db"


def connect(db: Path = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db))
    conn.execute(
        "CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, task TEXT NOT NULL, done INTEGER DEFAULT 0, created TEXT)"
    )
    conn.commit()
    return conn


def add(task: str, db: Path = DB_PATH) -> int:
    conn = connect(db)
    cur = conn.execute(
        "INSERT INTO todos (task, done, created) VALUES (?, 0, ?)",
        (task, datetime.now().isoformat(timespec="seconds")),
    )
    conn.commit()
    tid = cur.lastrowid
    conn.close()
    return tid


def list_todos(show_all: bool = False, db: Path = DB_PATH) -> list[tuple]:
    conn = connect(db)
    q = "SELECT id, task, done, created FROM todos"
    if not show_all:
        q += " WHERE done = 0"
    q += " ORDER BY id"
    rows = conn.execute(q).fetchall()
    conn.close()
    return rows


def complete(todo_id: int, db: Path = DB_PATH) -> bool:
    conn = connect(db)
    cur = conn.execute("UPDATE todos SET done = 1 WHERE id = ?", (todo_id,))
    conn.commit()
    ok = cur.rowcount > 0
    conn.close()
    return ok


def remove(todo_id: int, db: Path = DB_PATH) -> bool:
    conn = connect(db)
    cur = conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    ok = cur.rowcount > 0
    conn.close()
    return ok


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Todo list CLI.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add"); a.add_argument("task", nargs="+")
    ls = sub.add_parser("list"); ls.add_argument("-a", "--all", action="store_true")
    c = sub.add_parser("done"); c.add_argument("id", type=int)
    r = sub.add_parser("remove"); r.add_argument("id", type=int)
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.cmd == "add":
        tid = add(" ".join(args.task))
        print(f"Added todo #{tid}")
    elif args.cmd == "list":
        rows = list_todos(show_all=args.all)
        if not rows:
            print("No todos.")
            return 0
        for tid, task, done, created in rows:
            mark = "x" if done else " "
            print(f"[{mark}] {tid}: {task}  ({created})")
    elif args.cmd == "done":
        print("Done." if complete(args.id) else f"Todo #{args.id} not found.")
    elif args.cmd == "remove":
        print("Removed." if remove(args.id) else f"Todo #{args.id} not found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
