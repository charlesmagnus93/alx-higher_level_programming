#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for i, l in enumerate(my_list):
        if l == search:
            new_list.append(replace)
        else:
            new_list.append(l)
    return new_list
