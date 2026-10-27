import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_chart():
    out = main.chart([1,2,3])
    assert out.count("\n") == 2
    assert "3" in out

def test_empty():
    assert main.chart([]) == ""
