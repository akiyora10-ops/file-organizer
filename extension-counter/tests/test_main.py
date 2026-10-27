import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_count(tmp_path):
    import main
    from pathlib import Path
    (tmp_path/"a.txt").write_text("x"); (tmp_path/"b.txt").write_text("y"); (tmp_path/"c.png").write_bytes(b"")
    assert main.count(tmp_path)[".txt"]==2
