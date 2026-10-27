import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_find(tmp_path):
    import main
    from pathlib import Path
    (tmp_path/"a.txt").write_text("")
    (tmp_path/"b.txt").write_text("x")
    assert len(main.find(tmp_path))==1
