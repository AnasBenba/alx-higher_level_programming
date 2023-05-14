#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    length = len(my_list)
    n = 0
    new_list = [0] * length

    while n < length:
        if my_list[n] % 2 == 0:
            new_list[n] = True
            n += 1
        else:
            new_list[n] = False
            n += 1
    return new_list
