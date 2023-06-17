#!/usr/bin/python3
"""class Base"""
import json


class Base:
    """Base class for object management"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
        id (int): The ID of the object. If provided,
                  the object's ID is set to the given value.
                  If not provided, the object's ID is automatically
                  assigned based on the __nb_objects counter.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries to be converted.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            cls: The class object.
            list_objs: A list of objects to be serialized and saved.

        Returns:
            None

        Raises:
            None
        """
        class_name = cls.__name__
        my_dict = []
        if list_objs is None:
            list_objs = []
        for obj in list_objs:
            if isinstance(obj, Base):
                my_dict.append(obj.to_dictionary())
        with open("{}.json".format(class_name), 'w') as file:
            json.dump(my_dict, file)
