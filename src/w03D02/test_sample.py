"""Sample Test."""


def inc(x):
    """Increment."""
    return x + 1


def test_inc1():
    """Test Increment."""
    assert inc(3) != 5


def test_inc2():
    """Test Increment."""
    assert inc(3) == 4
