import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_count():
    import main
    assert main.count("Hello World")==3
