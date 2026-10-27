import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_stats():
    s = main.stats("hello world\nfoo")
    assert s["words"] == 3
    assert s["lines"] == 2
    assert s["chars"] > 0

def test_top_words():
    assert main.top_words("a a b", 1)[0] == ("a", 2)
