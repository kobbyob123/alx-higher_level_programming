#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    t_Values = []
    for i in my_list:
        if i % 2 == 0:
            t_Values.append(1)
        else:
            t_Values.append(0)
    return t_Values
