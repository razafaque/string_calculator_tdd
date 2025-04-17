import pytest
from calculator.string_calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number():
    assert add("1") == 1

def test_two_numbers():
    assert add("1,2") == 3

def test_multiple_numbers():
    assert add("1,2,3,4") == 10

def test_newline_delimiter():
    assert add("1\n2,3") == 6

def test_custom_delimiter_semicolon():
    assert add("//;\n1;2") == 3

def test_custom_delimiter_pipe():
    assert add("//|\n1|2|3") == 6

def test_negative_number_throws():
    with pytest.raises(ValueError, match="negative numbers not allowed -2"):
        add("1,-2,3")

def test_multiple_negatives_throws():
    with pytest.raises(ValueError, match="negative numbers not allowed -2,-4"):
        add("1,-2,-4,3")
