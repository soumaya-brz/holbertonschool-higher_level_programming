#!/usr/bin/python3
"""
That a module that contains say_my_name is a function that print
"My name is" with the first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that print My name is <first name> <last name>

    Args:
        first_name (str): The first name
        last_name (str): The last name

    Raises:
        TypeError: If first_name is not a string
        TypeError: If last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
