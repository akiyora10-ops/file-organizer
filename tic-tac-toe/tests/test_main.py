import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_win():
    b=["X"]*9
    # top row win
    b=["X","X","X","","","","","",""]
    assert main.check_winner(b)=="X"

def test_draw():
    b=["X","O","X","X","O","O","O","X","X"]
    assert main.check_winner(b)=="draw"

def test_move():
    b=[""]*9
    assert main.move(b,0,"X")
    assert not main.move(b,0,"O")
