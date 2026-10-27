import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_sample(tmp_path):
    import main, random
    from pathlib import Path
    random.seed(1)
    p=tmp_path/"d.csv"; p.write_text("n\n1\n2\n3\n4\n5\n")
    assert len(main.sample(p,3))==3
