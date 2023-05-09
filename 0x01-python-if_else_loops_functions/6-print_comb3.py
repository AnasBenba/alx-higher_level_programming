#!/usr/bin/python3
i = 0

while i < 9:
    j = i + 1

    while j <= 9:
        if i != 8:
            print("{:d}".format(i), end="")
            print("{:d}, ".format(j), end="")
            j += 1
        else:
            print("{:d}{:d}".format(i, j))
            j += 1
    i += 1
