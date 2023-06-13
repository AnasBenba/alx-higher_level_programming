#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """
    representing a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object with the provided
        first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Converts the Student object to a dictionary.

        Returns:
            dict: A dictionary representation of the Student object.
        """
        if attrs is None:
            return self.__dict__

        my_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                my_dict[attr] = getattr(self, attr)
        return my_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with the values from the provi
ed dictionary.

        Args:
            json (dict): A dictionary containing attribute names and their values.
        """
        for attr, value in json.items():
            setattr(self, attr, value)
