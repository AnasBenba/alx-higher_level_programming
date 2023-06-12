#!/usr/bin/python3
"""function that see if the object is exactly
an instance of the specified class"""


def is_same_class(obj, a_class):
    """Returns True or False"""
    return type(obj) is a_class
