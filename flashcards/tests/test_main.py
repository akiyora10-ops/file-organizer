import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_study():
    cards=[{"q":"a","a":"b"},{"q":"c","a":"d"}]
    assert main.study(cards,1)==2
