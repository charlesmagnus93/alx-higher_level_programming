#!/usr/bin/python3
"""
no module
"""


def inherits_from(obj, a_class):
    """return bool"""
    if issubclass(obj.__class__, a_class) is True:
        if obj.__class__ is not a_class:
            return True
    else:
        return False
