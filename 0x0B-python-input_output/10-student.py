#!/usr/bin/python3
"""
no module
"""


class Student:
    """student definition"""
    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieve dictionary"""
        if type(attrs) == list and all(type(el) == str for el in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
