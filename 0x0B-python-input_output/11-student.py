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
        return self.__dict__

    def reload_from_json(self, json):
        """replaces"""
        for key, value in json.items():
            setattr(self, key, value)
