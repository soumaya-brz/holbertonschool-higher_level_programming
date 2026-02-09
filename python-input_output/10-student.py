#!/usr/bin/python3
"""Module that defines a Student class with filtered to_json method."""


class Student:
    """Defines a student with first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance.

        If attrs is a list of strings, only returns keys present in this list.
        Otherwise, returns all attributes.
        """
        if isinstance(attrs, list):
            filtered = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered[attr] = getattr(self, attr)
            return filtered
        return self.__dict__.copy()
