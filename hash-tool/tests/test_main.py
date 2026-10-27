import hashlib, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main
from pathlib import Path

def test_hash_text():
    assert main.hash_text("abc", "md5") == hashlib.md5(b"abc").hexdigest()

def test_hash_file(tmp_path):
    p = tmp_path / "f.txt"; p.write_text("hello")
    assert main.hash_file(p, "sha256") == hashlib.sha256(b"hello").hexdigest()
