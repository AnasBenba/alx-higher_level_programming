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
    return max(my_list)
