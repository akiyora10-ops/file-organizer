import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_stopwatch():
    sw = main.Stopwatch()
    sw.start_timer()
    time.sleep(0.05)
    sw.stop()
    assert sw.time() >= 0.04
    sw.reset()
    assert sw.time() == 0.0
