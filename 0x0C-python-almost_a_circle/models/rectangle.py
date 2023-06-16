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
        self.__width = None
        self.__height = None
        self.__x = None
        self.__y = None

        self.width = width
        self.height = height
        self.x = x
        self.y = y

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

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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

        Raises:
            TypeError: If x is not an integer.
            ValueError: If x is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y-coordinate of the rectangle's position.

        Returns:
            int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y-coordinate of the rectangle's position.

        Args:
            value (int): The new y-coordinate value.

        Raises:
            TypeError: If y is not an integer.
            ValueError: If y is less than
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        result = self.__width * self.__height
        return result

    def display(self):
        """
        Prints a rectangle with the specified width and
        height using the '#' character.
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        Returns a string representation of the
        rectangle in the following format:
        [Rectangle] (id) x/y - width/height
        """
        string = "[Rectangle] ({}) {}/{} - {}/{}"
        return string.format(self.id, self.__x, self.__y,
                             self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle with the provided arguments.

        Args:
            *args: Variable number of arguments to update the
                   attributes in the following order:
                    - Argument 1: id (optional)
                    - Argument 2: width (optional)
                    - Argument 3: height (optional)
                    - Argument 4: x (optional)
                    - Argument 5: y (optional)
            **kwargs: Keyword arguments to update the attributes
            by specifying attribute names as keys.

        Note:
            If both positional arguments and keyword arguments are
            provided, the keyword arguments take precedence.


        """
        if len(args) >= 1:
            self.id = args[0]
        else:
            for key in kwargs.keys():
                if key == 'id':
                    self.id = kwargs[key]
                if key == 'width':
                    self.width = kwargs[key]
                if key == 'height':
                    self.height = kwargs[key]
                if key == 'x':
                    self.x = kwargs[key]
                if key == 'y':
                    self.y = kwargs[key]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

    def to_dictionary(self):
        """
        Converts the attributes of the Rectangle to a dictionary.

        Returns:
            dict: A dictionary containing the attributes of the Rectangle.
        """
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['width'] = self.width
        my_dict['height'] = self.height
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        return my_dict
