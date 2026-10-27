import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_minutes():
    import main
    assert main.minutes("a "*200)==1.0
