#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delims = ['.', ':', '?']
    for delim in delims:
        lines = [line.strip() for line in text.split(delim)]
        text = (delim + "\n\n").join(lines)
    print(text, end="")

