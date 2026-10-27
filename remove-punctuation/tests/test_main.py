import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_clean():
    import main
    assert main.clean("Hello, world!")=="Hello world"
