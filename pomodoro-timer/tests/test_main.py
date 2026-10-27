import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_run():
    phases = main.run(25,5,2)
    assert len(phases)==4
    assert phases[0]=="work 25m"
