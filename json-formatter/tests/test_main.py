import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_format():
    out = main.format_json('{"b":1,"a":2}', sort_keys=True)
    assert '"a": 2' in out and '"b": 1' in out

def test_minify():
    assert main.minify('{"a": 1}') == '{"a":1}'

def test_invalid():
    assert main.main(["{bad}"]) == 1
