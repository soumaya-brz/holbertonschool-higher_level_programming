#!/usr/bin/python3
"""Defines a function that returns the list of available attributes and methods of an object."""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: any Python object

    Returns:
        list of attributes and methods
    """
    return dir(obj)
