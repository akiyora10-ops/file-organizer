import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_stats():
    import main, statistics
    assert main.main(["1","2","3"])==0
