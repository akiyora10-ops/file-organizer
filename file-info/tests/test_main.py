import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_info(tmp_path):
    import main
    from pathlib import Path
    f=tmp_path/"a.txt"; f.write_text("hi")
    assert main.info(f)["size"]==2
