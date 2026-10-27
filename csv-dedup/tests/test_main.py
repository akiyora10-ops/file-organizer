import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_dedup(tmp_path):
    import main
    from pathlib import Path
    p=tmp_path/"d.csv"; p.write_text("name\nA\nA\nB\n")
    rows=main.dedup(p,"name")
    assert len(rows)==2
