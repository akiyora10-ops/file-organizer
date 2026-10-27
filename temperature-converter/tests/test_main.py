import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_cf():
    assert main.convert(0, "C", "F") == 32.0
    assert round(main.convert(100, "C", "F"), 1) == 212.0

def test_k():
    assert round(main.convert(0, "C", "K"), 2) == 273.15
