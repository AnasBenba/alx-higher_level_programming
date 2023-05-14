#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        length = len(row) - 1
        n = 0
        while n <= length:
            if n != length:
                print("{:d}".format(row[n]), end=' ')
                n += 1
            else:
                print("{:d}".format(row[n]), end='')
                n += 1
        print()
