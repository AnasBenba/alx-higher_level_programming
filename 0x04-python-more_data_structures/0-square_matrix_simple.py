#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    n = 0
    new_list = []
    for row in matrix:
        numbers = []
        for element in row:
            numbers.append(element ** 2)
        new_list.append(numbers)
    result = list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
    return result
