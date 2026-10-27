import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_play_correct():
    assert main.play(5, [3,5]) == "correct"

def test_play_lost():
    assert main.play(5, [1,2]) == "lost"
