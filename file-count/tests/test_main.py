import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_count(tmp_path):
    import main
    from pathlib import Path
    (tmp_path/"a.txt").write_text("x"); (tmp_path/"d").mkdir()
    assert main.count(tmp_path)==(1,1)
