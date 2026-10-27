import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_flatten():
    import main
    assert main.flatten({"a":{"b":1}})=={"a.b":1}
