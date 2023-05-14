#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    max_num = 0

    if length == 0:
        return "None"
    else:
        max_num = my_list[0]

        for n in my_list:
            if max_num < n:
                max_num = n
    return max_num
