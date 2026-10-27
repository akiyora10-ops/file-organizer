import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main
from pathlib import Path

def test_merge(tmp_path):
    a = tmp_path/"a.csv"; a.write_text("name,age\nAlice,30\n")
    b = tmp_path/"b.csv"; b.write_text("name,age\nBob,25\n")
    out = tmp_path/"out.csv"
    assert main.merge([a,b], out) == 2
    rows = list(csv.DictReader(out.open()))
    assert len(rows) == 2
    assert rows[0]["name"] == "Alice"
