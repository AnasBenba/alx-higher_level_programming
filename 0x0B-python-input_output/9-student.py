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

    def to_json(self):
        """
        Converts the Student object to a dictionary.

        Returns:
            dict: A dictionary representation of the Student object.
        """
        return self.__dict__
