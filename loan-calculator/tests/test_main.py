import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_payment():
    mp = main.monthly_payment(10000, 5, 12)
    assert 850 < mp < 860

def test_amortization():
    rows = main.amortization(1000, 0, 4)
    assert len(rows) == 4
    assert rows[-1]["balance"] == 0.0
