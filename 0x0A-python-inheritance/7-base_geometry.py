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
        """
        Validate if a value is an integer and greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        Returns:
            None
        """
        if type(value) != int
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
