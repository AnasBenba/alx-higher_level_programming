#!/usr/bin/python3 
from models.base import Base

"""class Rectangle that inherits from Base"""

class Rectangle(Base):
    """
    Represents a Rectangle that inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position (default: 0).
            y (int): The y-coordinate of the rectangle's position (default: 0).
            id (int): The ID of the rectangle (default: None).
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter method for the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width of the rectangle.

        Args:
            value (int): The new width value.
        """
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height of the rectangle.

        Args:
            value (int): The new height value.
        """
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x-coordinate of the rectangle's position.

        Returns:
            int: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x-coordinate of the rectangle's position.

        Args:
            value (int): The new x-coordinate value.
        """
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y-coordinate of the rectangle's position.

        Returns:
            int: The y-coordinate of the rectangle's position.
        """
        return self__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y-coordinate of the rectangle's position.

        Args:
            value (int): The new y-coordinate value.
        """
        self.__y = value
