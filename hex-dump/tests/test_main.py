import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_dump():
    import main
    out=main.dump(b"abc")
    assert "61 62 63" in out
