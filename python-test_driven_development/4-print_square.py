#!/usr/bin/python3
"""
That a module that contains print_square a function that print a square
of # in specifique size
"""


def print_square(size):
    """Print a square of a specifique size

    This function prints a square of # in specifique size
    to the standard output.

    Args:
        size (int): The size of the Square to be printed

    Returns:
        int: the number of # printed

    Raises:
        TypeError: If size is not a integer

    Example:
        >>> print_square(4)
        ####
        ####
        ####
        ####
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    elif size <= 0:
        raise ValueError("size must be >= 0")
    print('\n'.join(['#' * size for _ in range(size)]))
