import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_roundtrip():
    t = "hello world/?q=1"
    assert main.decode(main.encode(t)) == t

def test_qs():
    assert "a=1" in main.encode_qs({"a":1})
