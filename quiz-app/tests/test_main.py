import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_score():
    qs=[{"question":"2+2?","answer":"4"},{"question":"cap?","answer":"paris"}]
    assert main.score(qs, ["4","paris"])==2
    assert main.score(qs, ["5","paris"])==1
