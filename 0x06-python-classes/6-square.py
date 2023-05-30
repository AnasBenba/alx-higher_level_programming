#!/usr/bin/python3
"""module Square"""


class Square:
    """
    A class representing a square.

    Attributes:
        _Square__size (int): The size of the square.
        _Square__position (tuple): The position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes a
        Square instance with a given size and position.
        size(self): Getter method to retrieve the size of the square.
        size(self, value): Setter method to set the size of the square.
        position(self): Getter method to retrieve the position of the square.
        position(self, value): Setter method to set the position of the square.
        area(self): Calculates and returns the area of the square.
        my_print(self): Prints the square pattern using '#' characters.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int, optional): The size of the square (default is 0).
            position (tuple, optional): The position
            of the square (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self._Square__size = size
        self._Square__position = position

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

    @property
    def position(self):
        """
        Getter method to retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self._Square__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position of the square.

        Args:
            value (tuple): The new position for the square.

        Raises:
            TypeError: If position is not a tuple of
            2 positive integers.
        """
        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(self._Square__position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(self._Square__position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._Square__position = value

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
        The position parameter can be used to offset the square
        by adding spaces before the '#' characters.
        """
        if self._Square__size == 0:
            print()
        else:
            for j in range(self._Square__position[1]):
                print()
            for _ in range(self._Square__size):
                print(" " * self._Square__position[0] + "#" * self._Square__size)
