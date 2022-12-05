#!/usr/bin/python3

def resizetup(tup_a=(), tup_b=()):
    '''Compares two tuples and resizes the smallest
    to the size of the largest by filling in with 0'''
    if len(tup_a) > len(tup_b):
        c = -1 * (len(tup_a) - len(tup_b))
        list2 = []
        for i in range(len(tup_b)):
            list2.append(tup_b[i])
        for i in range(c, 0):
            list2.append(0)
        tup_b = tuple(list2)
        return tup_b

    elif len(tup_b) > len(tup_a):
        c = -1 * (len(tup_b) - len(tup_a))
        list3 = []
        for i in range(len(tup_a)):
            list3.append(tup_a[i])
        for i in range(c, 0):
            list3.append(0)
        tup_a = tuple(list3)
        return tup_a


def add_tuple(tuple_a=(), tuple_b=()):
    sum = []
    if len(tuple_a) > len(tuple_b):
        a = tuple_a
        b = resizetup(tuple_a, tuple_b)
    elif len(tuple_b) > len(tuple_a):
        a = tuple_b
        b = resizetup(tuple_a, tuple_b)
    else:
        a = tuple_a
        b = tuple_b
    sum = [a[0] + b[0], a[1] + b[1]]
    return tuple(sum)
