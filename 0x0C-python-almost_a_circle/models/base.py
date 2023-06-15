#!/usr/bin/python3
"""class Base"""


class Base:
    """Base class for object management"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
        id (int): The ID of the object. If provided,
                  the object's ID is set to the given value.
                  If not provided, the object's ID is automatically
                  assigned based on the __nb_objects counter.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
