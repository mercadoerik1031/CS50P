from plates import is_valid

def test_valid_plate():
    assert is_valid("ABC123") == True
    assert is_valid("XYZ678") == True
    assert is_valid("BCD234") == True

def test_invalid_plate():
    assert is_valid("AB123CD") == False
    assert is_valid("XYZ6789") == False
    assert is_valid("BCD@34") == False

def test_start():
    assert is_valid("AB123C") == False
    assert is_valid("123ABC") == False
    assert is_valid("ABC12") == True

def test_length():
    assert is_valid("AB123C") == False
    assert is_valid("AB1C") == False

def test_punctuation():
    assert is_valid("AB123C") == False
    assert is_valid("AB 123C") == False

def test_number():
    assert is_valid("AB123C") == False
    assert is_valid("ABC") == True
    assert is_valid("ABC0") == False

def test_middle():
    assert is_valid("AB123C") == False
    assert is_valid("A1B2C3") == False
    assert is_valid("AB12C3") == False
