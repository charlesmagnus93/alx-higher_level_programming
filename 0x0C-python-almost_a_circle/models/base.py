#!/usr/bin/python3
"""
no module
"""


class Base:
    """
    Base definition
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
