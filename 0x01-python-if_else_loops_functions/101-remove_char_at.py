#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str):
        return str
    new_string = ""
    for s in range(len(str)):
        if s != n:
            new_string += str[s]

    return new_string

