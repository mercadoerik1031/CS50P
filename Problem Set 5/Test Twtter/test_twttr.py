from twttr import shorten


def test_empty_string():
    assert shorten("") == ""

def test_no_vowels():
    assert shorten("hello") == "hll"

def test_with_vowels():
    assert shorten("python") == "pythn"

def test_mixed_case():
    assert shorten("Apples") == "ppls"

def test_all_vowels():
    assert shorten("AEIOUaeiou") == ""

def test_numbers_and_symbols():
    assert shorten("123$@.") == "123$@."