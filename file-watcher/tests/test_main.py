import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_hash(tmp_path):
    import main
    from pathlib import Path
    f=tmp_path/"a.txt"; f.write_text("hi")
    assert len(main.file_hash(f))==64
