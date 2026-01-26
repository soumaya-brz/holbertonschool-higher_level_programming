#!/usr/bin/python3
"""Module that defines a Square class with private size and accessors."""


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
        self.size = size  # utilise le setter pour valider

    @property
    def size(self):
        """Getter method for the private size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the private size attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
