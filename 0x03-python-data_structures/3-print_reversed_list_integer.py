#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    numEle = len(my_list) - 1

    for i in range(numEle, -1, -1):
        p = print("{:d}".format(my_list[i]))
