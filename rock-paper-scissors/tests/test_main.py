import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_winner():
    assert main.winner("rock","scissors")=="a"
    assert main.winner("rock","rock")=="tie"
    assert main.winner("rock","paper")=="b"
