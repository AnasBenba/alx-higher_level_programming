#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    length = len(my_list) - 1
    n = 0
    value = my_list[idx]
    if idx < 0 or idx >= length:
        return my_list
    while n <= length:
        if n == idx:
            my_list.remove(value)
            break
        n += 1
    return my_list
