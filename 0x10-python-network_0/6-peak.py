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
    first = 0
    mid = 1
    last = 2
    peak = my_list[0]

    while (last < len(my_list)):
        if my_list[mid] == peak:
            mid += 1
            first += 1
            last += 1
        elif my_list[mid] >= my_list[first]:
            if my_list[mid] >= my_list[last]:
                if peak < my_list[mid]:
                    peak = my_list[mid]
        mid += 1
        first += 1
        last += 1
    return peak
