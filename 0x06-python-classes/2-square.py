#!/usr/bin/python3
"""
no module
"""


class Square:
    """
    Square definition
    """
    def __init__(self, size=0) -> None:
        """
        Initialization
        """
        try:
            if (isinstance(size, int)):
                self.__size = size
                if size < 0:
                    raise ValueError('size must be >= 0')
            else:
                raise TypeError('size must be an integer')
        except Exception as ex:
            print(ex)
