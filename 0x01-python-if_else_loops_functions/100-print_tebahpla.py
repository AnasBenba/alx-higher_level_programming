#!/usr/bin/python3
flag = 0
for num in reversed(range(97, 123)):
    if flag == 0:
        flag = 1
        char = chr(num)
        print("{}".format(char), end="")
    elif flag != 0:
        flag = 0
        c = chr(num-32)
        print("{}".format(c), end="")

