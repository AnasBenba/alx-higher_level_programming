#!/usr/bin/python3
"""module Square"""


class Square:
    """
    A class representing a square.

    Attributes:
        _Square__size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a
        Square instance with a given size.
        size(self): Getter method to retrieve the size of the square.
        size(self, value): Setter method to set the size of the square.
        area(self): Calculates and returns the area of the square.
        my_print(self): Prints the square pattern using '#' characters.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self._Square__size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._Square__size ** 2

    def my_print(self):
        """
        Prints the square pattern using '#' characters.

        If the size of the square is 0, it prints an empty line.
        Otherwise, it prints a pattern of '#' characters forming a square.
        """
        i = 0
        if self._Square__size == 0:
            print()
        else:
            while i < self._Square__size:
                print("#" * self._Square__size)
                i += 1
