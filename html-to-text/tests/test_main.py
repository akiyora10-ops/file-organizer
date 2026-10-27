import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_strip():
    out = main.strip_tags("<p>Hello <b>world</b>!</p>")
    assert "Hello" in out and "world" in out
    assert "<" not in out

def test_no_tags():
    assert "<" not in main.strip_tags("<p>x</p>")

def test_entities():
    assert main.strip_tags("&amp;") == "&"
