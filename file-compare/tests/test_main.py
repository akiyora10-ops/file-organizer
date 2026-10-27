import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main
from pathlib import Path

def test_compare_identical(tmp_path):
    a = tmp_path/"a.txt"; a.write_text("x\n")
    b = tmp_path/"b.txt"; b.write_text("x\n")
    assert main.compare(a,b) == ""

def test_similarity(tmp_path):
    a = tmp_path/"a.txt"; a.write_text("abc")
    b = tmp_path/"b.txt"; b.write_text("abc")
    assert main.similarity(a,b) == 1.0
