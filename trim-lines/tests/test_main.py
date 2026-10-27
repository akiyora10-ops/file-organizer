import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_trim():
    import main
    assert main.trim("  a  \n  b  ")=="a\nb"
