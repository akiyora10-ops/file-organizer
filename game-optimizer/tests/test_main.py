import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import main

def test_profiles():
    from core.profiles import get_profile, list_profiles
    p = get_profile("Counter-Strike 2")
    assert "launch_options" in p
    assert "Counter-Strike 2" in list_profiles()

def test_cpu():
    from core.benchmark import cpu_usage, memory_usage
    assert isinstance(cpu_usage(), float)
    assert "percent" in memory_usage()

def test_detector():
    from core.detector import detect_all
    assert isinstance(detect_all(), list)
