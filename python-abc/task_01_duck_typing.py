#!/usr/bin/python3
"""
Module defining an abstract base class Shape and its concrete implementations
Circle and Rectangle. The module also includes a function shape_info that
demonstrates duck typing by accepting any object that implements the area
and perimeter methods.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape."""

    def __init__(self, radius):
        """Initialize a circle with a given radius."""
        self.radius = abs(radius)

    def area(self):
        """Calculate and return the area of the circle."""
        return pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the perimeter of the circle."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""

    def __init__(self, width, height):
        """Initialize a rectangle with given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape using duck typing."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
