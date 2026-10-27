import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_convert(tmp_path):
    import main
    from pathlib import Path
    p=tmp_path/"d.csv"; p.write_text("a,b\n1,2\n")
    assert "| a | b |" in main.convert(p)
