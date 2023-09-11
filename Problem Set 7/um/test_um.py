from um import count

def test_count_um():
    # Test cases with different occurrences of "um"
    assert count("hello, um, world") == 1
    assert count("yummy") == 0
    assert count("Um is um, but UM") == 3

def test_count_um_case_insensitive():
    # Test case with case-insensitive matching
    assert count("UM UM um") == 3

def test_count_um_no_word_boundary():
    # Test cases where "um" is part of a larger word or substring
    assert count("album") == 0
    assert count("humble") == 0
    assert count("umbrella") == 0
    assert count("I'm not sure what to do") == 0

def test_count_um_multiple_occurrences():
    # Test case with multiple "um" occurrences in a single string
    assert count("um um um") == 3

if __name__ == "__main__":
    import pytest
    pytest.main()
