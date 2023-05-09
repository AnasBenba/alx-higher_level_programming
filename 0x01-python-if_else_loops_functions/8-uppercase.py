#!/usr/bin/python3
def uppercase(str):
    for s in str:
        char = ord(s)
        if char >= 97 and char <= 122:
            char -= 32
        print("{:c}".format(char), end="")
    print()
