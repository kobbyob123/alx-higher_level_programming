#!/usr/bin/python3

'''def safe_print_integer(value):
    try:
        if value.isdigit() == 0:
            ret_val = 0
    except Exception:
        ret_val = 1
        print(value)
    return ret_val'''

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
