import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_to_base():
    assert main.to_base(255, 16) == "FF"
    assert main.to_base(10, 2) == "1010"

def test_roundtrip():
    assert main.from_base(main.to_base(100, 8), 8) == 100
