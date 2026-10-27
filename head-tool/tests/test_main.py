import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_head(tmp_path):
    import main
    from pathlib import Path
    p=tmp_path/"f.txt"; p.write_text("1\n2\n3\n4")
    assert main.head(p,2)==["1","2"]
