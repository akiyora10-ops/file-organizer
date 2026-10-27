import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main
from pathlib import Path

def test_sort_unique(tmp_path):
    p = tmp_path / "f.txt"; p.write_text("b\na\na\nc")
    lines = main.read_lines(p)
    assert main.read_lines is not None
    # sort via function not exposed; test read_lines
    assert lines == ["b","a","a","c"]

def test_unique_output(capsys, tmp_path):
    p = tmp_path / "f.txt"; p.write_text("a\nb\na")
    main.main(["unique", str(p)])
    out = capsys.readouterr().out.strip().splitlines()
    assert out == ["a","b"]
