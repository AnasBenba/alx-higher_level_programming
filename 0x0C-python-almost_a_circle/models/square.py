#!/usr/bin/python3
from models.rectangle import Rectangle

"""class Square that inherits from Rectangle"""


class Square(Rectangle):
    """
    Represents a square, which is a special case of a rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a square with the given size, position, and optional id.

        Args:
            size (int): The size of the square (both width and height).
            x (int): The x-coordinate of the square's position (default: 0).
            y (int): The y-coordinate of the square's position (default: 0).
            id (Any): The optional id of the square (default: None).
        """
        super().__init__(id=id, x=x, y=y, width=size, height=size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The formatted string representation of the square.
        """
        string = "[Square] ({}) {}/{} - {}"
        return string.format(self.id, self.x, self.y, self.width)
