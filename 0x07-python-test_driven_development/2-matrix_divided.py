#!/usr/bin/python3
"""
No module
"""


def matrix_divided(matrix, div):
    """
        a function that divides all elements of a matrix
    """
    new_matrix = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for element in matrix:
        tmp = []
        if len(matrix[0]) != len(element):
            raise TypeError("Each row of the matrix must have the same size")
        for el in element:
            if type(el) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
            el = round(el / div, 2)
            tmp.append(el)
        new_matrix.append(tmp)
    return new_matrix

