import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_pangram():
    import main
    assert main.is_pangram("The quick brown fox jumps over the lazy dog")
    assert not main.is_pangram("hello")
