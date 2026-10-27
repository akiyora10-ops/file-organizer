import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_roundtrip():
    t = "Attack at dawn!"
    assert main.decrypt(main.encrypt(t, "KEY"), "KEY") == t
