#!/usr/bin/python3
""" Rectangle class"""


class Rectangle:
    """
    Represent a rectangle

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        int: The width of the rectangle.
        """
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the width value is not an integer.
            ValueError: If the width value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        """
        int: The height of the rectangle.
        """
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the height value is not an integer.
            ValueError: If the height value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float or int: The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.height):
            if i == self.height - 1:
                rectangle_str += str(self.print_symbol) * self.width
            else:
                rectangle_str += str(self.print_symbol) * self.width + "\n"
        return rectangle_str

    def __repr__(self):
        """
        Return a string representation of the rectangle
        that can be used to recreate the object.

        Returns:
            str: The string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Perform cleanup actions when the rectangle
        object is about to be destroyed.

        This method is automatically called by the garbage collector
        when the objectis no longer referenced.

        Returns:
            None
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the
        rectangle with the bigger area, or the
        first rectangle if their areas are equal.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The rectangle with the bigger
            area or the first rectangle if equal.

        Raises:
            TypeError: If either rect_1 or rect_2 is
            not an instance of the Rectangle class.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
