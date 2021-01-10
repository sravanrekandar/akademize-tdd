"""Pallindrome."""
from test_reverse_of_a_number_sol_2 import get_reverse


def is_pallindrome(n):
    """Is pallindrome."""
    return get_reverse(n) == n


def test_pallindrome():
    """Test Is Pallindrome."""
    assert is_pallindrome(1234) is False
    assert is_pallindrome(1221) is True
