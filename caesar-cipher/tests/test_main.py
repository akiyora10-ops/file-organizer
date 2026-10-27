import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_roundtrip():
    t = "Hello, World!"
    assert main.decrypt(main.encrypt(t, 5), 5) == t

def test_brute():
    assert len(main.brute_force("abc")) == 26
