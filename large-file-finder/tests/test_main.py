import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_find(tmp_path):
    import main
    from pathlib import Path
    (tmp_path/"big.bin").write_bytes(b"x"*100)
    assert len(main.find(tmp_path, 0))==1
