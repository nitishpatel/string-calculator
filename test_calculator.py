from calculator import add

def test_empty_string_returns_zero():
    """Test that an empty string returns zero."""
    assert add("") == 0
