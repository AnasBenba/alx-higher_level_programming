#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length_a = len(tuple_a)
    length_b = len(tuple_b)
    new_tuple_a = [num for num in tuple_a]
    new_tuple_b = [num for num in tuple_b]
    result = [0, 0]
    n = 0

    if length_a == 0:
        new_tuple_a = [0, 0]
    elif length_a < 2:
        new_tuple_a = new_tuple_a + [0]

    if length_b == 0:
        new_tuple_b = [0, 0]
    elif length_b < 2:
        new_tuple_b = new_tuple_b + [0]

    while n < 2:
        a = new_tuple_a[n]
        b = new_tuple_b[n]
        result[n] = a + b
        n += 1
    new_tuple = tuple(result)
    return new_tuple
