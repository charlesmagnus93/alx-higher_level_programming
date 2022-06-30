#!/usr/bin/python3
from sys import argv
if len(argv) == 1:
    print('{} arguments.'.format(len(argv) - 1))
elif len(argv) == 2:
    print('{} argument.'.format(len(argv) - 1))
    print('{}: {}'.format(len(argv) - 1, argv[1]))
else:
    print('{} arguments.'.format(len(argv) - 1))
    for i, arg in enumerate(argv, start=0):
        if i == 0:
            continue
        print('{}: {}'.format(i, argv[i]))

if __name__ == "__main__":
    argv
