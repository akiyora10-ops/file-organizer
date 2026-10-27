import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_sort(tmp_path):
    import main, csv
    from pathlib import Path
    p=tmp_path/"d.csv"; p.write_text("name,age\nBob,25\nAlice,30\n")
    rows,_=main.sort_csv(p,"name")
    assert rows[0]["name"]=="Alice"
