#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if value.isdigit() == 0:
            ret_val = 0
    except AttributeError:
        ret_val = 1
        print(value)
    return ret_val
