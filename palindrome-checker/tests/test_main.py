import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_pal():
    import main
    assert main.is_palindrome("A man a plan a canal Panama")
    assert not main.is_palindrome("hello")
