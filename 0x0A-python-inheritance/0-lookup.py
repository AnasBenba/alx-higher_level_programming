#!/usr/bin/python3

def lookup(obj):
     """
    Retrieves a list of attributes and methods available for an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of attribute and method names.
    """
    return dir(obj)
