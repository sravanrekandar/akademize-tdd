"""Factorial"""


def factorial(n):
    """Get the factorial of a given number.

    Args
    ----
    n : an integer

    Returns
    ------
    Returns an integer
    """

    fact = 1
    i = n
    while i > 1:
        fact *= i
        i -= 1

    return fact
