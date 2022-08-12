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
        self.__width = value

    @property
    def height(self):
        """retrieve"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        self.__height = value

    @property
    def x(self):
        """retrieve"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        self.__x = value

    @property
    def y(self):
        """retrieve"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        self.__y = value
