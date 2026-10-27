import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_roundtrip():
    for n in [1,4,9,42,1999,3999]:
        assert main.from_roman(main.to_roman(n)) == n

def test_invalid():
    try:
        main.to_roman(0); assert False
    except ValueError:
        pass
