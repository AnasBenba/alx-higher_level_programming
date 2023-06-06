#!/usr/bin/python3
class LockedClass:
    """A class that prevents the creation of new instance
    attributes, except for 'first_name'."""
    __slots__ = ('first_name')

    def __setattr__(self, name, value):
        """
        Set the value of an attribute on
        the LockedClass instance.

        Args:
            name (str): The name of the attribute.
            value: The value to be assigned to the attribute.

        Raises:
            AttributeError: If the attribute
            name is not 'first_name'.
        """
        if name != 'first_name':
            raise AttributeError("'LockedClass' object \
has no attribute 'last_name'")
        super().__setattr__(name, value)
