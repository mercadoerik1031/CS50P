from seasons import minutes_to_str, convert_to_minutes


def test_minute_to_string():
    assert minutes_to_str(525600) == "Five hundred twenty-five thousand, six hundred minutes"


def test_convert_to_minutes():
    assert convert_to_minutes(365) == 525600