from numb3rs import validate

def test_working():
    assert validate("11.22.33.44") == True
    assert validate("44.33.22.11") == True

def test_not_working():
    assert validate("277.33.299.2") == False
    assert validate("1.5.34.300") == False
