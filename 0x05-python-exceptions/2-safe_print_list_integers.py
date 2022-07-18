#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        for a in range(x):
            if (isinstance(my_list[a], int)):
                i = i + 1
                # print('iccci', list(range(x)))
                print("{:d}".format(my_list[a]), end="")
            else:
                # print(my_list[a])
                continue
        print('')
        return i
    except Exception as err:
        pass
