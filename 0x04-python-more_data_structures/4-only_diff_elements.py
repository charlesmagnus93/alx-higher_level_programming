#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    el = []
    for x in set_1:
        if (x in set_2):
            continue
        else:
            el.append(x)
    for y in set_2:
        if (y in set_1):
            continue
        else:
            el.append(y)
    return el
