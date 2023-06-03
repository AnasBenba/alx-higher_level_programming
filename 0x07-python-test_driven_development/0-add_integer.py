#!/usr/bin/python3
"""
function add_integer

this function takes two integers or floats
"""


def add_integer(a, b=98):
    """
    returns an integer the addition of a and b
    """
    _a = a
    _b = b

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        _a = int(a)
    if isinstance(b, float):
        _b = int(b)
    return _a + _b
