import zipfile, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main
from pathlib import Path

def test_list(tmp_path):
    zp = tmp_path/"a.zip"
    with zipfile.ZipFile(zp, "w") as z:
        z.writestr("f.txt", "hi")
    assert main.list_zip(zp) == [("f.txt", 2)]

def test_extract(tmp_path):
    zp = tmp_path/"a.zip"
    with zipfile.ZipFile(zp, "w") as z:
        z.writestr("f.txt", "hi")
    out = tmp_path/"out"; out.mkdir()
    assert main.extract(zp, out) == 1
    assert (out/"f.txt").read_text() == "hi"
