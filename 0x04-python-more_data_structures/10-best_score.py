#!/usr/bin/python3

def best_score(a_dictionary):
    best = 0
    name = ''
    if a_dictionary is None:
        return None
    else:
        keys = sorted(a_dictionary)
        for x in keys:
            if a_dictionary[x] > best:
                best = a_dictionary[x]
                name = x
    return name
