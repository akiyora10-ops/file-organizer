import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_info():
    import main
    assert main.info("localhost")["ip"] in ("127.0.0.1","::1")
