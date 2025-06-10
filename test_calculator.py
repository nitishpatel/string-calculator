from calculator import StringCalculator
import pytest

string_calc = StringCalculator()
def test_empty_string_returns_zero():
    """Test that an empty string returns zero."""
    assert string_calc.add("") == 0


def test_single_number_returns_value():
    """Test that a single number returns its value."""
    assert string_calc.add("9") == 9


def test_two_numbers_return_sum():
    """Test that two numbers return their sum."""
    assert string_calc.add("1,4") == 5

def test_invalid_number_raises_exception():
    """Test that an invalid number raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid number: abc"):
        string_calc.add("1,abc")

def test_multiple_numbers_return_sum():
    """Test that multiple numbers return their sum."""
    assert string_calc.add("10,20,30,40,50") == 150

def test_newline_between_numbers():
    """Test that numbers separated by newlines are summed correctly."""
    assert string_calc.add("1\n2,10") == 13

def test_custom_delimiter():
    """Test that a custom delimiter works."""
    assert string_calc.add("//;\n1;2;3") == 6
    assert string_calc.add("//|\n1|2|3|4") == 10

def test_negative_number_raises_exception():
    """Test that a negative number raises a ValueError."""
    with pytest.raises(ValueError, match="negative numbers not allowed -3"):
        string_calc.add("1,-3")

def test_multiple_negatives_show_all():
    with pytest.raises(ValueError, match="negative numbers not allowed -1, -2, -3"):
        string_calc.add("1,-1,2,-2,3,-3")

