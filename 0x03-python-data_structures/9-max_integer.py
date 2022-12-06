#!/usr/bin/python3

def max_integer(my_list=[]):
    num1 = len(my_list)
    if num1 == 0:
        return None

    for i in range(num1):
        for j in range(num1):
            if my_list[i] < my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
    # print(my_list)
    return my_list[-1]
