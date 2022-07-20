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
        except Exception:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        """
        retrieve private attri
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set private sttri
        """
        self.__size = value
        try:
            assert (isinstance(value, int))
        except Exception:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """
        Area of Square
        """
        return self.__size ** 2
