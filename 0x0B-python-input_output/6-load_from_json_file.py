#!/usr/bin/python3
"""
Creating an object from JSON file
"""

import json


def load_from_json_file(filename):
    """
    Loading a python object from a json file
    Return:
    object: he python object loaded ffrom JSON file
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
