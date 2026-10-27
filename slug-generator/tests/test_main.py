import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_slugify():
    assert main.slugify("Hello World!") == "hello-world"
    assert main.slugify("Café au lait") == "cafe-au-lait"
    assert main.slugify("a   b") == "a-b"
