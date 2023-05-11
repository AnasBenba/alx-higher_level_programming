#!/usr/bin/python3
import sys


def main():
    length = len(sys.argv) - 1

    if length == 0:
        print("{} arguments.".format(length))

    if length > 0:
        n = 1

        print("{} arguments:".format(length))

        while n <= length:
            print("{}: {}".format(n, sys.argv[n]))
            n += 1


if __name__ == "__main__":
    main()
