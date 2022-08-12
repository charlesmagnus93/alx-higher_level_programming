#!/usr/bin/python3
"""
Square inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square extends from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor for square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """str representation of square"""
        return '[Square] ({}) {}/{} - {}'.format(
            self.id,
            self.x,
            self.y,
            self.size
        )

    @property
    def size(self):
        """retrieve """
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update"""
        if (args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                elif i == 3:
                    self.y = j
        for key, value in kwargs.items():
            setattr(self, key, value)
