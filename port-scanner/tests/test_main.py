import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_parse():
    import main
    assert main.parse_ports("1-3")==[1,2,3]
    assert main.parse_ports("80,443")==[80,443]
