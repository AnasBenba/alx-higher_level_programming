#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str) or first_name == "":
        raise TypeError("first_name must be a string")
    if any(char.isdigit() for char in first_name):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if any(char.isdigit() for char in last_name):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
