import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_convert():
    xml = "<root><a>1</a><b x='2'>3</b></root>"
    out = main.convert(xml)
    data = json.loads(out)
    assert data["root"]["a"] == "1"
    assert data["root"]["b"]["#text"] == "3"

def test_invalid():
    assert main.main(["<bad"]) == 1
