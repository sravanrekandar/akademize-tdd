"""Test Is_Armstrong."""

from is_armstrong import is_armstrong


def test_is_armstrong():
    """Test Is Armstrong."""
    assert is_armstrong(153) is True
    assert is_armstrong(370) is True
    assert is_armstrong(371) is True
    assert is_armstrong(407) is True
    assert is_armstrong(1) is True
    assert is_armstrong(5) is True
    assert is_armstrong(500) is False
    assert is_armstrong(665) is False
    assert is_armstrong(1634) is True
