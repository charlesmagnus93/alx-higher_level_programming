#!/usr/bin/python3
"""
no module
"""

def read_file(filename=""):
    """read text file and print out"""
    with open(filename, encoding="utf-8") as s:
        for line in s:
            print(line, end="")
