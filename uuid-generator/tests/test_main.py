import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_gen():
    import main
    us=main.gen(3)
    assert len(us)==3
    assert all(len(u)==36 for u in us)
