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
        json_str = cls.to_json_string(my_dict)
        with open("{}.json".format(class_name), 'w') as file:
            json.dump(my_dict, file)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string to a list of dictionaries.

        Args:
            json_string (str): The JSON string to be converted.

        Returns:
            list: A list of dictionaries if the JSON string
            represents a valid list of dictionaries.
            An empty list if the JSON string is None or
            represents an invalid list of dictionaries.
            None if the JSON string is not a list.

        Raises:
            None
        """
        if json_string is None:
            return []
        my_list = json.loads(json_string)
        if type(my_list) == list:
            for item in my_list:
                if not isinstance(item, dict):
                    return
        return my_list

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of the class with all attributes
        already set based on the provided dictionary.

        Args:
            **dictionary: A dictionary containing attribute-value pairs.

        Returns:
            An instance of the class with attributes
            set based on the dictionary.

        Raises:
            None.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load instances of the class from a file in JSON format.

        Returns:
            list: A list of instances of the class loaded from the file.
        """
        class_name = "{}.json".format(cls.__name__)
        try:
            with open(class_name, 'r') as file:
                string = file.read()
                my_list = cls.from_json_string(string)
                instances = []
                for data in my_list:
                    instances.append(cls.create(**data))
                return instances
        except FileNotFoundError:
            return []
