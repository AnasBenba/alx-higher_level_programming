#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list == []:
        return []

    new_list = my_list.copy()
    n = 0
    length = len(new_list)

    while n < length:
        if new_list[n] == search:
            new_list[n] = replace
        n += 1
    return new_list
