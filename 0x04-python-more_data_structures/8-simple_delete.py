#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    sort = sorted(a_dictionary)
    for x in sort:
        if x == key:
            a_dictionary.pop(key)
    return a_dictionary
