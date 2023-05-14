#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if my_list == []:
        return my_list

    length = len(my_list) - 1
    value = my_list[idx]

    if idx < 0 or idx > length:
        return my_list
    my_list.remove(value)
    return my_list
