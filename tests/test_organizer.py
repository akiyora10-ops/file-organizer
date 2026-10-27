import tempfile
from pathlib import Path
from file_organizer.organizer import organize_by_extension, group_for_ext

def test_group_for_ext():
    assert group_for_ext(".PNG") == "images"
    assert group_for_ext(".xyz") == "other"

def test_organize_by_extension(tmp_path):
    (tmp_path / "a.png").write_text("x")
    (tmp_path / "b.txt").write_text("y")
    moves = organize_by_extension(tmp_path)
    assert len(moves) == 2
    assert (tmp_path / "images" / "a.png").exists()
    assert (tmp_path / "documents" / "b.txt").exists()
