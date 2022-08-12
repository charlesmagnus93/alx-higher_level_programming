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
