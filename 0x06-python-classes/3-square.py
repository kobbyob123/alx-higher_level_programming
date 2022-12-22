#!/usr/bin/python3
"""A module about a Square"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        self.__size = size

        if type(size) == int:
            pass
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates area of a Square

        Returns:
            int: area of a Square
        """
        return self.__size * self.__size
