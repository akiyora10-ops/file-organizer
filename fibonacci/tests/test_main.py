import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_fibonacci():
    assert main.fibonacci(7) == [0,1,1,2,3,5,8]

def test_nth():
    assert main.fib(10) == 55
