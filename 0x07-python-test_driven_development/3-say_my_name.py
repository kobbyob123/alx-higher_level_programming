#!/usr/bin/python3
""" A module that prints your name
"""


def say_my_name(first_name, last_name=""):
    """Return a string saying your name

    Args:
        first_name (str): first name
        last_name (str, optional): _description_. Defaults to "".

    Raises:
        TypeError: When input is not a string
        TypeError: When input is not a string

    Returns:
        str: A sentence saying <your full name>
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
