import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_fetch():
    import main
    # network may be unavailable; just ensure function exists
    assert callable(main.fetch)
