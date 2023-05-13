#!/usr/bin/python3

def element_at(my_list, idx):
    length = len(my_list)

    if idx < 0 or idx >= length:
        return "None"
    else:
        num = my_list[idx]
        return num
