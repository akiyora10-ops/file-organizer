import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_valid():
    import main
    assert main.is_valid("a@b.com")
    assert not main.is_valid("bad@")
