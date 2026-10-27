from timer.countdown import parse_duration, format_remaining

def test_parse_duration():
    assert parse_duration("30") == 30
    assert parse_duration("2m") == 120
    assert parse_duration("1h") == 3600
    assert parse_duration("5 min") == 300

def test_format_remaining():
    assert format_remaining(65) == "01:05"
    assert format_remaining(3661) == "01:01:01"
