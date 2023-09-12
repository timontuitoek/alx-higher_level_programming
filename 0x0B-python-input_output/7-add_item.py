#!/usr/bin/python3
"""
Load, add, save
"""


import sys


def save_to_json_file(my_obj, filename):
    """
    defining a function to save [ython object to JSON file
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)

    """
    defining function to load a python from a jSon file
    """
    with open(filename, mode='f', encoding='utf-8') as file:
        return json.load(file)
