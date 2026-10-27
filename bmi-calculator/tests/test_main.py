import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_bmi():
    assert round(main.bmi(70, 1.75), 2) == 22.86

def test_category():
    assert main.category(17) == "underweight"
    assert main.category(22) == "normal"
    assert main.category(27) == "overweight"
    assert main.category(32) == "obese"
