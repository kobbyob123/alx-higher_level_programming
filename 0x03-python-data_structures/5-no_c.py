#!/usr/bin/env python3

def no_c(my_string):
    newStr = ""

    for i in my_string:
        if (i == 'c') or (i == 'C'):
            continue

        else:
            newStr = newStr + i

    return newStr
