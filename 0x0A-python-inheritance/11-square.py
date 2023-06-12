#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""
    def __init__(self, size):
        """
        Initializes a Square object with the given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.

        Returns:
            None
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the square.

        Args:
            None

        Returns:
            str: The string representation of the square
            in the format '[Square] <size>/<size>'.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
