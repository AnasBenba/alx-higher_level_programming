#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


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

    @property
    def size(self):
        """
        The size of the square (both width and height).

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square (both width and height).

        Args:
            value (int): The size value to set.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square with the provided arguments.

        Args:
            *args: Variable number of positional arguments to
                   update the attributes in the following order:
                 - Argument 1: id (optional)
                 - Argument 2: size (optional)
                 - Argument 3: x (optional)
                 - Argument 4: y (optional)
            **kwargs: Keyword arguments to update the attributes
                      by specifying attribute names as keys.

        Note:
            If both positional arguments and keyword arguments are provided,
            the keyword arguments take precedence.
        """
        if len(args) >= 1:
            self.id = args[0]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]

    def to_dictionary(self):
        """
        Converts the attributes of the square to a dictionary.

        Returns:
            dict: A dictionary containing the attributes of the square.
        """
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['size'] = self.size
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        return my_dict
