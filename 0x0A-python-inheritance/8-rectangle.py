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


class Rectangle(BaseGeometry):
    """
    Rectangle class, inherits from BaseGeometry.

    This class represents a rectangle
    shape and provides methods for calculating
    its area and validating the width and height.

    Attributes:
        None

    Methods:
        __init__(self, width, height): Initializes a
        rectangle object with the given width and height.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangle object with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.

        Returns:
            None
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
