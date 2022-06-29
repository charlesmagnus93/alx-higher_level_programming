#!/usr/bin/python3
from dis import dis


def magic_calculation(a, b):
    a + b
    return 98


dis(magic_calculation)
