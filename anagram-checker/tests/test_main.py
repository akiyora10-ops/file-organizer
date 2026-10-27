import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_anagram():
    import main
    assert main.is_anagram("listen","silent")
    assert not main.is_anagram("hello","world")
