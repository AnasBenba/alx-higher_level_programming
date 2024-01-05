#!/usr/bin/python3
'''
function that finds a peak in a list of unsorted integers.
'''


def find_peak(list_of_integers):
    '''
    function that finds a peak in a list of unsorted integers.
    '''
    my_list = list_of_integers
    if len(my_list) == 0:
        return None
    if len(my_list) == 1:
        return my_list[0]
    if len(my_list) == 2:
        return max(my_list)

    mid = len(my_list) // 2

    if my_list[mid] > my_list[mid - 1] and my_list[mid] > my_list[mid + 1]:
        return my_list[mid]
    elif my_list[mid] < my_list[mid - 1]:
        return find_peak(my_list[:mid])
    else:
        return find_peak(my_list[mid + 1:])
