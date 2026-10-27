import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_table():
    import main
    t=main.table(2,3)
    assert t==[[1,2,3],[2,4,6]]
