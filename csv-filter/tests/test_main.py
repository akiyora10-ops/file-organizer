import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main
from pathlib import Path

def test_filter(tmp_path):
    p = tmp_path/"d.csv"; p.write_text("name,age\nAlice,30\nBob,25\n")
    rows = main.filter_rows(p, "age", "gt", "26")
    assert len(rows) == 1 and rows[0]["name"] == "Alice"
    rows2 = main.filter_rows(p, "name", "contains", "Bo")
    assert len(rows2) == 1
