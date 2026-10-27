import os, sys
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_age():
    y, m, d = main.age(date(2000,1,1), date(2020,1,1))
    assert y == 20 and d == 7305

def test_months():
    y, m, d = main.age(date(2000,1,1), date(2000,3,1))
    assert m == 2
