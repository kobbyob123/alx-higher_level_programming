#!/usr/bin/python3

for idx in range(89):
    if (int(idx/10)) == (idx % 10):
        continue

    if int(idx/10) > (idx % 10):
        continue

    else:
        print("{}{}, ".format(int(idx/10), idx % 10), end="")

print(89)
