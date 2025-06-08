from calculator import add
import pytest


def test_empty_string_returns_zero():
    """Test that an empty string returns zero."""
    assert add("") == 0


def test_single_number_returns_value():
    """Test that a single number returns its value."""
    assert add("9") == 9


def test_two_numbers_return_sum():
    """Test that two numbers return their sum."""
    assert add("1,4") == 5

def test_invalid_number_raises_exception():
    """Test that an invalid number raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid number: abc"):
        add("1,abc")
