import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_lookup():
    import main, socket
    # localhost resolves
    assert isinstance(main.lookup("localhost"), str)
