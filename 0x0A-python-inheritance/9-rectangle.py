#!/usr/bin/python3
"""
no module
"""


class BaseGeometry:
    """Base"""

    def area(self):
        """area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        x = type(value)
        if x is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle inherits from Base"""

    def __init__(self, width, height):
        """initialization"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """area"""
        return self.__width * self.__height

    def __str__(self):
        """str representation"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
