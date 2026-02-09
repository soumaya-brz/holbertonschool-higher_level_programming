#!/usr/bin/python3
"""Module that defines a Student class with JSON serialization and reload."""


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

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance with values from json."""
        for key, value in json.items():
            setattr(self, key, value)
