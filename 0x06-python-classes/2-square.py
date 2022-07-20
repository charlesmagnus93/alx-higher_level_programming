#!/usr/bin/python3
"""
no module
"""


class Square:
    """
    Square definition
    def __init__(self, size=0):
    """
    def __init__(self, size=0):
        """
        Initialization
        --------
        size: interger
        """
        self.__size = size
        try:
            assert (isinstance(size, int))
        except TypeError:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
