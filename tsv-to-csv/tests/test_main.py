import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_convert(tmp_path):
    import main
    from pathlib import Path
    p=tmp_path/"d.tsv"; p.write_text("a\tb\n1\t2\n")
    out=tmp_path/"d.csv"
    assert main.convert(p,out)==2
    assert out.read_text().strip()=="a,b\n1,2"
