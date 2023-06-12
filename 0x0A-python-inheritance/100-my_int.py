#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    def __eq__(self, value):
        """
        Overrides the equality operator '=='.

        Args:
            value: The value to compare with.

        Returns:
            bool: Always returns False, indicating instances
            of MyInt are never equal to any value.
        """
        return False

    def __ne__(self, value):
        """
        Overrides the inequality operator '!='.

        Args:
            value: The value to compare with.

        Returns:
            bool: Always returns True, indicating
            instances of MyInt are always not equal to any value.
        """
        return True
