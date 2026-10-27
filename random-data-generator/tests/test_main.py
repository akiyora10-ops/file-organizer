import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_generate():
    data = main.generate(3, ["name","email","age"])
    assert len(data) == 3
    assert all("name" in d and "email" in d for d in data)
    assert all(18 <= d["age"] <= 80 for d in data)

def test_email_format():
    e = main.random_email()
    assert "@" in e and "." in e.split("@")[1]
