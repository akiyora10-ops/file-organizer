import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main
from pathlib import Path

def test_merge(tmp_path):
    a = tmp_path/"a.txt"; a.write_text("hi")
    b = tmp_path/"b.txt"; b.write_text("bye")
    out = tmp_path/"out.txt"
    main.merge([a,b], out, separator="\n")
    assert out.read_text() == "hi\nbye"
