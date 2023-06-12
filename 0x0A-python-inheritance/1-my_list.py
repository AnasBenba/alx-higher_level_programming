#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """
    A custom list subclass that extends the built-in
    list class with additional functionality.
    """
    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.

        This method sorts the elements of the list in
        ascending order and prints them.
        Note that the original list is not modified.

        Example:
            my_list = MyList([3, 1, 2])
            my_list.print_sorted()  # Output: [1, 2, 3]
        """
        print(sorted(self))
