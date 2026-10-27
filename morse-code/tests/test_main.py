import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_roundtrip():
    t = "HELLO WORLD"
    assert main.decode(main.encode(t)) == t

def test_encode_sos():
    assert "..." in main.encode("SOS")
