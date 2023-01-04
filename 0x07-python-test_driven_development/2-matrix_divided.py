#!/usr/bin/python3
"""This module divides contains the functions for matrix operations
"""


def matrix_divided(matrix, div):
    """Divides every element in the matrix by 'div'

    Args:
        matrix (list): a list containing lists only
        div (int): the number by with every element in
        the matrix will be divided by

    Returns:
        list: a matrix with all elements divided by 'div'
    """
    if div is None:
        div = 1

    check_num(div)
    check_matrix(matrix)
    check_type(matrix)
    check_len(matrix)
    new, new_row = [], []

    for row in matrix:
        new_row = list(map(lambda x: round(x / div, 2), row))
        new.append(new_row)

    return new


def check_matrix(list1):
    """Checks if the input is a matrix(list containing lists)

    Args:
        list1 (list): a list

    Raises:
        TypeError: If input is not a list
        TypeError: if element of list is not a list

    Returns:
        None: Nothing
    """
    if type(list1) != list:
        raise TypeError("Must be a matrix to proceed")

    for i in range(len(list1)):
        if type(list1[i]) != list:
            raise TypeError("Must be a matrix to proceed")
    return None


def check_type(list1):
    """Checks if the elements of the matrix are ints or floats

    Args:
        list1 (list): a list containing lists

    Raises:
        TypeError: when the elements of the matrix are not ints or floats

    Returns:
        None: Nothing
    """
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            if type(list1[i][j]) not in [int, float]:
                raise TypeError("Must be an int or float")
    return None


def check_len(list1):
    """Checks if the rows of the matrix are all equal

    Args:
        list1 (list): a matrix

    Raises:
        TypeError: When rows are not equal

    Returns:
        None: Nothing
    """
    for i in range(len(list1)):
        for j in range(len(list1)):
            if i == j:
                break
            else:
                if len(list1[i]) != len(list1[j]):
                    raise
                TypeError("Each row of the matrix must have the same size")
    return None


def check_num(div):
    """Checks if div is an int or float

    Args:
        div (int/float): An integer or a float

    Raises:
        TypeError: When div is not an int or a float
        ZeroDivisionError: When div has value == 0

    Returns:
        None: Nothing
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return None


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
