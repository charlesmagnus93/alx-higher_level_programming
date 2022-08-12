#!/usr/bin/python3
"""
no module
"""
import json


class Base:
    """
    Base definition
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON string"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes into file"""
        file_name = cls.__name__ + ".json"
        the_list = []
        if list_objs is not None:
            for i in list_objs:
                the_list.append(cls.to_dictionary(i))
        with open(file_name, 'w') as json_file:
            json_file.write(cls.to_json_string(the_list))
