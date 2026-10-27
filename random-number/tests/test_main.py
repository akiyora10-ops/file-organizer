import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_gen():
    import main, random
    random.seed(1)
    vals=main.gen(0,5,3)
    assert all(0<=v<=5 for v in vals)
