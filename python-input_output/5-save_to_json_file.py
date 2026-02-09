#!/usr/bin/python3
"""Module that saves a Python object to a JSON file."""

import json


def save_to_json_file(my_obj, filename):
    """Writes a Python object to a file in JSON format."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
