import zipfile, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main
from pathlib import Path

def test_backup(tmp_path):
    src = tmp_path/"src"; src.mkdir()
    (src/"a.txt").write_text("hi")
    (src/"sub").mkdir(); (src/"sub"/"b.txt").write_text("x")
    dst = tmp_path/"backup.zip"
    assert main.backup(src, dst) == 2
    with zipfile.ZipFile(dst) as z:
        assert set(z.namelist()) == {"a.txt", "sub/b.txt"}
