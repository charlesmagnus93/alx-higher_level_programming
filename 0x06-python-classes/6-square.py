#!/usr/bin/python3
"""
no module
"""


class Square:
    """
    Square definition
    def __init__(self, size=0):
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization
        --------
        size: interger
        """
        self.__size = size
        self.__position = position
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
    
    @property
    def position(self):
        """
        retrieve private attrib position
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        set private attrib position
        """
        self.__position = value
        try:
            assert (isinstance(value, tuple))
        except Exception:
            raise TypeError('position must be a tuple of 2 positive integers')
        try:
            assert (isinstance(value[0], int)) or (isinstance(value[1], int))
        except Exception:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """
        Area of Square
        """
        return self.__size ** 2

    def my_print(self):
        """
        print square with caracter #
        """
        if self.__size == 0:
            print()
        for x in range(self.position[1]):
            print('\n')
        for x in range(self.__size):
            for y in range(self.position[0]):
                print(' ', end="")
            for y in range(self.__size):
                print('#', end="")
            print()