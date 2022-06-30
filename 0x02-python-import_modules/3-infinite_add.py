#!/usr/bin/python3
from sys import argv
a = 0
for i, arg in enumerate(argv, start=0):
    if i == 0:
        continue
    a += int(argv[i])
print('{}'.format(a))

if __name__ == "__main__":
    argv
