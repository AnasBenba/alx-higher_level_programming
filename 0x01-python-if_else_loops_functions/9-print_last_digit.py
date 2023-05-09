#!/usr/bin/python3
def print_last_digit(number):
    num = abs(number)
    result = num % 10
    print("{:d}".format(result), end="")
    return result
