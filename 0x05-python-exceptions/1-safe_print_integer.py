#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if any(type(el) == int for el in value):
            print("{:d}".format(value))
            return True
        else:
            return Exception
    except:
        return False
