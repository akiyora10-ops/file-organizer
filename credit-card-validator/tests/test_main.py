import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_luhn():
    import main
    assert main.luhn("4532015112830366")
    assert not main.luhn("1234567890123456")
