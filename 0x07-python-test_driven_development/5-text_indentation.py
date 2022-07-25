#!/usr/bin/python3
"""
    No module
"""


def text_indentation(text):
    """
        prints Text indentation
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for el in text:
        if el in ['.', '?', ':']:
            print(el, end='\n\n')
            continue
        print(el, end='')
