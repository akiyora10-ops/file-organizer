import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main
from pathlib import Path

def test_tree(tmp_path):
    (tmp_path/"a").mkdir()
    (tmp_path/"a"/"b.txt").write_text("x")
    (tmp_path/"c.txt").write_text("y")
    lines = main.tree(tmp_path, 2)
    assert any("a" in l for l in lines)
    assert any("b.txt" in l for l in lines)
