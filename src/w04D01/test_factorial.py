"""Tes factorial."""

from factorial import factorial


def test_factorial():
    """Test Factorial."""
    assert factorial(1) == 1
    assert factorial(3) == 6
    assert factorial(5) == 120
