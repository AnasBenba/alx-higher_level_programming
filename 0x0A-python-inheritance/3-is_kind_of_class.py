#!/usr/bin/python3
"""function that see if the object is an instance of,
or if the object is an instance of a class that inherited
from, the specified class"""


def is_kind_of_class(obj, a_class):
    """returns True or False"""
    return isinstance(obj, a_class)
