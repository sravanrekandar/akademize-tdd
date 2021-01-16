"""Test is_strong_number"""
from is_strong_number import is_strong_number


def test_is_strong_number():
    """Test is_strong_number."""
    assert is_strong_number(145) is True
    assert is_strong_number(146) is False
