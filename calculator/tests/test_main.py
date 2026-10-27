import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_basic():
    assert main.safe_eval("2 + 3 * 4") == 14
    assert main.safe_eval("(10-2)/4") == 2.0

def test_power():
    assert main.safe_eval("2**8") == 256

def test_invalid():
    try:
        main.safe_eval("__import__('os')")
        assert False
    except ValueError:
        pass
