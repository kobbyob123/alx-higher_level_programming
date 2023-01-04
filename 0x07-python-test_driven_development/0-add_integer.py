#!/usr/bin/python3
"""This module contains a function for adding two numbers
"""


def add_integer(a, b=98):
    """This function adds two numbers of type int

    Args:
        a (int or float): an integer
        b (int or float, optional): defaults to 98.
    """
    if (type(a) == int) or (type(a) == float):
        pass
    else:
        raise TypeError("a must be an integer")
    if (type(b) == int) or (type(b) == float):
        pass
    else:
        raise TypeError("b must be an integer")

    a, b = int(a), int(b)

    return a + b
