#!/usr/bin/python3
""" Prints a square
"""


def print_square(size):
    """This function prints an nxn square

    Args:
        size (int): The dimension of the square

    Raises:
        TypeError: When 'size' is not an int
        ValueError: When 'size' is less than 0 

    Returns:
        None: This function return None
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

    return None
