import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_day():
    import main
    assert main.weekday(__import__("datetime").date(2020,1,1))=="Wednesday"
