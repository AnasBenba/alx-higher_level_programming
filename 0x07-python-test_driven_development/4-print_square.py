#!/usr/bin/python3
"""
function prints a square

this function takes one integer
"""


def print_square(size):
    """
    prints a square of length size
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    i = 0
    while i < size:
        print("#" * size)
        i += 1
