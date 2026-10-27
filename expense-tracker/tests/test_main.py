import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_add_list(tmp_path):
    import main
    db = tmp_path / "t.db"
    main.DB = db
    # recreate connect path by monkey
    tid = main.add(["x", "x", "x"], db=db)
    assert tid == 1
    assert len(main.list_all(db=db)) == 1
