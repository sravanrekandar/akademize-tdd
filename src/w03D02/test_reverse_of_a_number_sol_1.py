"""Reverse of a given number."""


def get_reverse_sol_1(n):
    """Get reverse of a number."""

    return int(str(n)[::-1])


def test_get_reverse_sol_1():
    """Test get reverse of a number."""
    assert get_reverse_sol_1(1234) == 4321
    assert get_reverse_sol_1(3445) == 5443
