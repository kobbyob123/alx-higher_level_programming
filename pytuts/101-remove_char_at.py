#!/usr/bin/python3

def remove_char_at(str, n):
    counter = 0
    res = ""

    for i in str:
        if counter == n:
            i = ""
        res += i
        counter += 1
    return res
