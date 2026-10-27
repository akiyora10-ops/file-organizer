from PIL import Image
from pathlib import Path
from resizer.resizer import resize_image

def test_resize(tmp_path):
    src = tmp_path / "in.png"
    Image.new("RGB", (100, 50), "red").save(src)
    dst = tmp_path / "out.png"
    resize_image(src, dst, width=50)
    with Image.open(dst) as im:
        assert im.width == 50
        assert im.height == 25
