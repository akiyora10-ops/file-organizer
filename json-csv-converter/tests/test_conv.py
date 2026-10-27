import json
from pathlib import Path
from converter.conv import json_to_csv, csv_to_json

def test_roundtrip(tmp_path):
    data = [{"name": "a", "age": 1}, {"name": "b", "age": 2}]
    jf = tmp_path / "d.json"; jf.write_text(json.dumps(data))
    cf = tmp_path / "d.csv"
    assert json_to_csv(jf, cf) == 2
    jf2 = tmp_path / "d2.json"
    assert csv_to_json(cf, jf2) == 2
    assert json.loads(jf2.read_text()) == [{"name": "a", "age": "1"}, {"name": "b", "age": "2"}]
