#!/usr/bin/python3
"""function that see if the object is an instance of a class
that inherited (directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """Returns True or False"""
    if type(obj) is not a_class:
        return isinstance(obj, a_class)
