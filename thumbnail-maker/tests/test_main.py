from PIL import Image
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main
from pathlib import Path

def test_thumbnail(tmp_path):
    src = tmp_path/"in.png"; Image.new("RGB",(200,100),"blue").save(src)
    dst = tmp_path/"out.png"; main.make_thumbnail(src, dst, (50,50))
    with Image.open(dst) as im:
        assert im.width <= 50 and im.height <= 50
