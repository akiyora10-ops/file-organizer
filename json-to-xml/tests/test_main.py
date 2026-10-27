import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_convert():
    out = main.convert('{"root": {"a": "1"}}')
    assert "<root>" in out and "<a>1</a>" in out

def test_invalid():
    assert main.main(["[1,2]"]) == 1
