#!/usr/bin/python3
"""Module that converts a class instance to a dictionary for JSON serialization."""


def class_to_json(obj):
    """Returns the dictionary description of a class instance."""
    return obj.__dict__.copy()
