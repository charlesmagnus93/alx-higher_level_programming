#!/usr/bin/python3
from dis import dis


def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return b
    else:
        b = a
        return c
