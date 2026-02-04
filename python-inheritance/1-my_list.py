#!/usr/bin/python3
"""
Module that defines a class MyList that inherits from list.
The class has a method to print the list in sorted order.
"""


class MyList(list):
    """A class that inherits from list and has a method to print
    the list in sorted order.
    """
    def print_sorted(self):
        """Prints the list in sorted order."""
        print(sorted(self))
