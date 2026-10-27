from PIL import Image
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main
from pathlib import Path

def test_grayscale(tmp_path):
    src = tmp_path/"in.png"; Image.new("RGB",(10,10),"red").save(src)
    dst = tmp_path/"out.png"; main.apply_filter(src, dst, "grayscale")
    with Image.open(dst) as im:
        assert im.mode == "L"
