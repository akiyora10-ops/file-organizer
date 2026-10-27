import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_info():
    d = main.info()
    assert "platform" in d
    assert "python" in d
