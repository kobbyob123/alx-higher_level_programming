def safe_print_list(my_list=[], x=0):
    count = 0
    for i in my_list:
        count += 1
    try:
        for element in range(x):
            print(my_list[element], end="")
    except IndexError:
        pass
    if x < count:
        number = x
    elif (x > count) or (x == count):
        number = count
    print()
    return number
