#!/usr/bin/python3
"""
0-add_integer module
Provides function to add two integers
"""


def add_integer(a, b=98):
    """
    Returns the addition of a and b as integers
    Raises TypeError if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
