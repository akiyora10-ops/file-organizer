import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_is_prime():
    assert main.is_prime(2) and main.is_prime(97)
    assert not main.is_prime(1) and not main.is_prime(99)

def test_sieve():
    assert main.sieve(10) == [2,3,5,7]

def test_factorize():
    assert main.factorize(60) == [2,2,3,5]
