#!/usr/bin/python3
"""0-add_integer module
This module contains a function that adds two integers
or floats (converted to integers).
"""


def add_integer(a, b=98):
    """Add two integers and return the result.

    a and b must be integers or floats, otherwise raise TypeError.
    Floats are casted to integers before the addition.

    Returns an integer: a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
