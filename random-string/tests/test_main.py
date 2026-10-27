import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_gen():
    import main
    s=main.gen(5)
    assert len(s)==5
