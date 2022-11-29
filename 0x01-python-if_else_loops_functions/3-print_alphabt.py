#!/usr/bin/python3
for idx in range(97, 123):
    if idx == 101 or idx == 113:
        continue
    else:
        print("{}".format(chr(idx)), end ="")
