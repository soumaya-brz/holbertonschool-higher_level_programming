#!/usr/bin/python3
"""Module that defines a Square class with size and area methods."""


class Square:
    """Class that defines a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize a Square with optional size (default 0).

        Args:
            size (int): size of the square (default 0)

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
