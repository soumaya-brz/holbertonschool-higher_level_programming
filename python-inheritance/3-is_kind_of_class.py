#!/usr/bin/python3
"""Defines a function to check class or inherited class"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or inherited from it"""
    return isinstance(obj, a_class)
