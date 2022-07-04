#!/usr/bin/python3
def max_integer(my_list=[]):
    big = 0
    if len(my_list) > 0:
        for x in my_list:
            if x > big:
                big = x
        return big
    return None
