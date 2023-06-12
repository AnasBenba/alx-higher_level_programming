#!/usr/bin/python3
"""empty class"""


class BaseGeometry:
    """base geometry class"""
    def area(self):
        """
        Raises:
            Exception: This method is not implemented in the base class.

        Returns:
            None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
