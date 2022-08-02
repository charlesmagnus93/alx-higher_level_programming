#!/usr/bin/python3
"""
no module
"""
import json


def save_to_json_file(my_obj, filename):
    """writes object"""
    with open(filename, mode="w") as s:
        json.dump(my_obj, s)
