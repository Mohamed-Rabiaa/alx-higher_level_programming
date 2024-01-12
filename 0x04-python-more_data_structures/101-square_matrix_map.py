#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda x: x**2, matrix[i])) for i in range(len(matrix))]
