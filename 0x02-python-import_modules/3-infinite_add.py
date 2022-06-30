#!/usr/bin/python3
from sys import argv
a = 0
for i in list(argv[1]):
    a += int(i)
print('{}'.format(a))

if __name__ == "__main__":
    argv
