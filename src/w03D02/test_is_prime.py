"""Test is_prime."""


def is_prime(n):
    """Is Prime.
    ----
    Args:
        n : An integer
    Returns
        Boolean (Prime or not)
    """

    if n == 0 or n == 1:
        return "Invalid number"
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def test_is_prime_invalid_numbers():
    """Test case for is_prime invalid numbers."""
    assert is_prime(0) == "Invalid number"
    assert is_prime(1) == "Invalid number"


def test_is_prime_non_primes():
    """Test case for is_prime Non Primes."""
    assert is_prime(121) is False
    assert is_prime(122) is False
    assert is_prime(12222) is False


def test_is_prime_primes():
    """Test case for is_prime Primes."""
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(7) is True
    assert is_prime(127) is True
