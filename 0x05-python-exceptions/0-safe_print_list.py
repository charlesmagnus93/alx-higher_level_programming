#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        el = ""
        i = 0
        for a in range(x):
            i = i + 1
            el += str(my_list[a])
        print(el)
        return i
    except IndexError:
        print(el)
        return i - 1
