#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 and len(tuple_a) != 0:
        if len(tuple_b) < 2 and len(tuple_b) != 0:
            return (tuple_a[0] + tuple_b[0], 0)
        elif len(tuple_b) == 0:
            return (tuple_a[0], 0)
        else:
            return (tuple_a[0] + tuple_b[0], tuple_b[1])
    elif len(tuple_a) == 0:
        if len(tuple_b) < 2 and len(tuple_b) != 0:
            return (tuple_b[0], 0)
        elif len(tuple_b) == 0:
            return (0, 0)
        else:
            return (tuple_b[0], tuple_b[1])
    else:
        if len(tuple_b) < 2 and len(tuple_b) != 0:
            return (tuple_a[0] + tuple_b[0], tuple_a[1])
        elif len(tuple_b) == 0:
            return (tuple_a[0], tuple_a[1])
        else:
            return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])