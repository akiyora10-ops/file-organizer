import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main
from pathlib import Path

def test_split_lines(tmp_path):
    src = tmp_path/"f.txt"; src.write_text("1\n2\n3\n4\n5")
    n = main.split_lines(src, 2, tmp_path/"chunk")
    assert n == 3
    assert (tmp_path/"chunk_000.txt").read_text() == "1\n2\n"

def test_split_bytes(tmp_path):
    src = tmp_path/"f.bin"; src.write_bytes(b"abcdef")
    n = main.split_bytes(src, 2, tmp_path/"c")
    assert n == 3
