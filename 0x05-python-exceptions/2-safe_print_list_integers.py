def safe_print_list_integers(my_list=[], x=0):
    count, count_int, number = 0, 0, 0

    for i in my_list:
        count += 1
    for i in range(count):
        if type(my_list[i]) == int:
            count_int += 1

    try:
        '''if x > count:
            try:
                for i in range(count):
                    if type(my_list[i]) == int:
                        print(my_list[i], end="")
                raise IndexError("list out of range")
            finally:
                pass'''

        for i in range(x):
            if type(my_list[i]) == int:
                print(my_list[i], end="")
        print()
    except EOFError:
        pass

    if x < count:
        number = x
    elif x == count:
        number = count_int

    return number
