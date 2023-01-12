#!/usr/bin/python3

def print_last_digit(number):
    """Prints last digit of a number"""

    if number >= 0:
        res = number % 10

    else:
        res = abs(number) % 10

    print("{:d}".format(res), end="")
    return res
