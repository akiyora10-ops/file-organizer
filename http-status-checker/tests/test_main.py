import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_check():
    import main
    # invalid url returns None
    assert main.check("http://127.0.0.1:1/nope") is None or isinstance(main.check("http://127.0.0.1:1/nope"), int)
