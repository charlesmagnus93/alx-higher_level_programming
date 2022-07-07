#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    cal = 0
    sm = 0
    for x in my_list:
        cal += x[0] * x[1]
        sm += x[1]
    return cal / sm
