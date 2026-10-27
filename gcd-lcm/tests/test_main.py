import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_gcd():
    import main, math
    # call main returns 0
    assert main.main(["12","18"])==0
