#!/usr/bin/python3
def no_c(my_string):
    a = ''
    for x in my_string:
        if x == 'c' or x == 'C':
            continue
        else:
            a += x
    return a
