import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_freq():
    import main
    assert main.freq("a a b",2)[0]==("a",2)
