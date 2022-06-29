#!/usr/bin/python3
from dis import dis


def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return True
    else:
        b = a
        return c
