#!/usr/bin/python3
import sys


def factorial(n):
    """
    Computes the factorial of a non-negative integer.

    Parameters:
        n (int): Non-negative integer.

    Returns:
        int: Factorial of n.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)
