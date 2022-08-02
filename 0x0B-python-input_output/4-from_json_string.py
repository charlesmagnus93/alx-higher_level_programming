#!/usr/bin/python3
"""
no module
"""
import json


def from_json_string(my_str):
    """return object"""
    data = json.loads(my_str)
    return data
