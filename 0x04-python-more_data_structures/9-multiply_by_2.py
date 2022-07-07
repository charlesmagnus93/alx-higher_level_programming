#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    cp = a_dictionary.copy()
    sort = sorted(cp)
    for x in sort:
        cp[x] = cp[x] * 2
    return cp
