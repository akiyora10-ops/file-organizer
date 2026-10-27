import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main
from pathlib import Path

def test_dir_size(tmp_path):
    (tmp_path/"a.txt").write_text("hello")
    sub = tmp_path/"sub"; sub.mkdir()
    (sub/"b.txt").write_text("xx")
    assert main.dir_size(tmp_path) == 7

def test_human():
    assert "KB" in main.human(2048)
