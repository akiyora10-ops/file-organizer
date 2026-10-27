import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main
from pathlib import Path

def test_text_roundtrip():
    assert main.decode_text(main.encode_text("hello")) == "hello"

def test_file_roundtrip(tmp_path):
    src = tmp_path / "a.txt"; src.write_text("hi")
    enc = tmp_path / "a.b64"; main.encode_file(src, enc)
    out = tmp_path / "b.txt"; main.decode_file(enc, out)
    assert out.read_text() == "hi"
