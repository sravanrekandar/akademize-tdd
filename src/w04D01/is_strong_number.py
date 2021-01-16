"""Is Strong Number.

Strong number is a special number whose sum of
factorial of digits is equal to the original number.

For example: 145 is strong number. Since, 1! + 4! + 5! = 145
"""
from factorial import factorial


def is_strong_number(n):
    sum = 0
    for c in str(n):
        sum += factorial(int(c))

    return sum == n
