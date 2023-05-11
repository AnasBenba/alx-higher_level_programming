#!/usr/bin/python3
import sys


def main():
    length = len(sys.argv) - 1

    if length == 0:
        print("{} arguments.".format(length))

    elif length == 1:
        print("{} argument:".format(length))
        print("{}: {}".format(length, sys.argv[1]))

    else:
        n = 1

        print("{} arguments:".format(length))

        while n <= length:
            print("{}: {}".format(n, sys.argv[n]))
            n += 1


if __name__ == "__main__":
    main()
