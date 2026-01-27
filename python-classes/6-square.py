#!/usr/bin/python3
"""Defines a Square class with size and position"""


class Square:
    """Represents a square with a size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square

        Args:
            size (int): size of the square
            position (tuple): (x, y) position for printing
        """
        self.size = size       # appel du setter
        self.position = position  # appel du setter

    @property
    def size(self):
        """Getter: retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: set the size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter: retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter: set the position with validation"""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):  # lignes vides en haut
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)  # espaces + #
