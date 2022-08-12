#!/usr/bin/python3
"""
module Rectangle inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieve"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieve"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieve"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieve"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of rectangle"""
        return self.__width * self.__height
