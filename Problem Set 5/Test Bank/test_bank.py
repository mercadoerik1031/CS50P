from bank import value


def test_hello():
    assert value("hello") == 0


def test_h():
    assert value("How are you") == 20


def test_no_h():
    assert value("What's up") == 100