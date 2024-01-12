#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        sq_row = list(map(lambda x: x**2, i))
        new_matrix.append(sq_row)
    return new_matrix
