import tempfile
from pathlib import Path
from todo_cli.todo import connect, add, list_todos, complete

def test_todo_flow(tmp_path):
    db = tmp_path / "t.db"
    tid = add("buy milk", db=db)
    assert tid == 1
    rows = list_todos(db=db)
    assert len(rows) == 1
    assert complete(tid, db=db)
    assert list_todos(db=db) == []
    assert list_todos(show_all=True, db=db)[0][2] == 1
