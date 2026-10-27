import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_roundtrip():
    ts = 1700000000
    s = main.to_human(ts)
    assert main.to_timestamp(s) == ts

def test_now():
    assert isinstance(main.now_ts(), int)
