import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_find_matches():
    ms = main.find_matches(r"\d+", "a1 b22")
    assert [m.group(0) for m in ms] == ["1","22"]

def test_invalid_regex():
    import io, contextlib
    # main returns 1
    assert main.main([r"[", "abc"]) == 1
