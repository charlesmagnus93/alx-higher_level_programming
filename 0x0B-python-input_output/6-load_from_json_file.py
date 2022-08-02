#!/usr/bin/python3
"""
no module
"""
import json


def load_from_json_file(filename):
    """create an Object"""
    with open(filename, "r") as s:
        return json.load(s)
