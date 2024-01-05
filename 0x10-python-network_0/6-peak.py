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
    if len(my_list) == 2:
        return max(my_list)
    del my_list[0]
    del my_list[len(my_list) - 1]
    value = max(my_list)
    return value
