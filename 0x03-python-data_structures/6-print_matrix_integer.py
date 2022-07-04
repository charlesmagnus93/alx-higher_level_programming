#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = ''
    for x in matrix:
        for y in x:
            a += '{:d} '.format(y)
        print('{}'.format(a).rstrip())
        a = ''
