#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    length = len(sys.argv) - 1

    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = sys.argv[1]
    operator = sys.argv[2]
    b = sys.argv[3]

    if operator not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if length == 3:
        result = 0

        if operator == '+':
            result = add(int(a), int(b))

        if operator == '-':
            result = sub(int(a), int(b))

        if operator == '*':
            result = mul(int(a), int(b))

        if operator == '/':
            result = div(int(a), int(b))

        print("{} {} {} = {}".format(a, operator, b, result))
        exit(0)


if __name__ == "__main__":
    main()
