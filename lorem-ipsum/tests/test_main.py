import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_generate():
    t = main.generate(2, 2, 4)
    assert t.count("\n\n") == 1
    assert t.endswith(".")

def test_sentence():
    s = main.sentence(5)
    assert s[0].isupper() and s.endswith(".")
