#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    dicti = dict(sorted(a_dictionary.items()))
    for key in dicti:
        value = dicti[key]
        print("{}: {}".format(key, value))
