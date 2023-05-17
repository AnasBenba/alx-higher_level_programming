#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return "None"
    max_value = max(a_dictionary, key=lambda k: a_dictionary[k])
    return max_value

