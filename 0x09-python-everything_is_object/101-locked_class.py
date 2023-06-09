#!/usr/bin/python3
class LockedClass:
    """A class that prevents the creation of new instance
    attributes, except for 'first_name'."""
    __slots__ = ('first_name') 
