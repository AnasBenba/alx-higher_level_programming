#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
