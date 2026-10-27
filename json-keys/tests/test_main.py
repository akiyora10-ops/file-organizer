import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_keys():
    import main
    assert "a" in main.keys({"a":1,"b":{"c":2}})
    assert "b.c" in main.keys({"a":1,"b":{"c":2}})
