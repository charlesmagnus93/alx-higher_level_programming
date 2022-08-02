#!/usr/bin/python3
"""
no module
"""


def write_file(filename="", text=""):
    """write file"""
    with open(filename, encoding="utf-8", mode="w+") as s:
        return s.write(text)
