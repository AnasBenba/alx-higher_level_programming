#!/usr/bin/python3
import sys


def main():
    lenght = len(sys.argv) - 1
    n = 1
    sum1 = 0

    while n <= lenght:
        sum1 += int(sys.argv[n])
        n += 1

    print("{}".format(sum1))


if __name__ == "__main__":
    main()
