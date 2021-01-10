"""Is Armstrong.
Armstrong number is a number that is
the sum of its own digits each raised to the power of the number of digits.

n = 153
number of digits in the number = 3
1^3 + 5^3 + 3^3 = 153

Other armstrong numbers
370
371
407
"""


def is_armstrong(n):
    """Is Armstrong."""
    num_digits = len(str(n))
    sum = 0
    for c in str(n):
        sum += int(c) ** num_digits
    return sum == n
