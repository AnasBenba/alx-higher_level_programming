#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """ prints to stdout"""
    with open(filename, "r") as file:
        contant = file.read()
        print(contant, end="\n")
