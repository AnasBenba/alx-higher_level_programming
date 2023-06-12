#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""
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
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Args:
            None

        Returns:
            int: The calculated area of the rectangle.
        """
        result = self.__width * self.__height
        return result

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Args:
            None

        Returns:
            str: The string representation of the rectangle
            in the format '[Rectangle] <width>/<height>'.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
