import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_main():
    import main
    assert main.main([".","-p","8080"])==0
