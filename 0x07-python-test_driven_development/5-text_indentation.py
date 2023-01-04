#!/usr/bin/python3
""" This prints a newline anytime a ['.', ':', '?'] is encountered
"""


def text_indentation(text):
    """Prints a newline anytime a ['.', ':', '?'] is encountered

    Args:
        text (string): The string to be processed

    Returns:
        None: Does not return anything
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0

    while i < len(text):
        print(text[i], end="")

        if text[i] in ".?:":
            print("\n")

        if (text[i] in ".?:") and (text[i+1] == ' '):
            i += 1

        i += 1

    return None
