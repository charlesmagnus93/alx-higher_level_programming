#!/usr/bin/python3
"""
no module
"""


def append_write(filename="", text=""):
    """appends a string at end"""
    with open(filename, encoding="utf-8", mode="a+") as s:
        return s.write(text)
