#!/usr/bin/python3

def matrix_divided(matrix, div):
    new_matrix = []

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    for row in matrix:
        new_row = []
        for elem in row:
            new_row.append(elem)
        new_matrix.append(new_row)

    length = 0
    for row in new_matrix:
        length += len(row)
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if length % 2 != 0:
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    for row in new_matrix:
        for i in range(len(row)):
            row[i] = round(row[i]/div, 2)

    return new_matrix
