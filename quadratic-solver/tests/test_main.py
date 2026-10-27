import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_solve():
    import main
    r1,r2=main.solve(1,-3,2)
    assert r1==2 and r2==1
