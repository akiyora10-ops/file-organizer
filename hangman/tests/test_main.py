import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_mask():
    assert main.mask("cat", {"c","t"}) == "c _ t"

def test_won():
    assert main.is_won("cat", {"c","a","t"})

def test_lost():
    assert main.is_lost(6)
    assert not main.is_lost(5)
