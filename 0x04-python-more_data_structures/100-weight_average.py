#!/usr/bin/python3

def weight_average(my_list=[]):
    cal = 0
    sm = 0
    for x in my_list:
        cal += x[0] * x[1]
        sm += x[1]
    return cal / sm
