import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_tail(tmp_path):
    import main
    from pathlib import Path
    p=tmp_path/"f.txt"; p.write_text("1\n2\n3\n4")
    assert main.tail(p,2)==["3","4"]
