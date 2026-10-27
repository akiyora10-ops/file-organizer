import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_norm():
    import main
    assert "a" in main.normalize("a/../a")
