import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_render():
    out = main.render("A")
    assert out.count("\n") == 4
    assert "A" in out

def test_unknown():
    out = main.render("1")
    assert "?" in out
