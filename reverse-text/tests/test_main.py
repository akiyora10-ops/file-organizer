import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_rev():
    import main
    assert main.rev("abc")=="cba"
