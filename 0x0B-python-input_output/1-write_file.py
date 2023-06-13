#!/usr/bin/python3
"""function that writes a string to a text file"""


def write_file(filename="", text=""):
    """returns the number of characters written"""
    character_len = 0
    with open(filename, "w") as file:
        file.write(text)
        return len(text)
