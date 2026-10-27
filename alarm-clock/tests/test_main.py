import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_seconds_until():
    assert main.seconds_until("23:59") >= 0
