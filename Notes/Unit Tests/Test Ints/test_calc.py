# from calc import square

# def main():
#     test_square()


# def test_square():
#     assert square(2) == 4 # assert checks if the statement is true else it give you san error
#     assert square(3) == 9

# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------------------------------

# pytest 3rd party program you can download and install
# will automate the tests as long as I write the tests

from calc import square
import pytest


# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0

# tets numbers separately
def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")