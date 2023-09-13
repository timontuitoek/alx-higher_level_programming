#!/usr/bin/python3
"""
Load, add, save
"""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_items():
    """
    adds all arguments to a python list
    """
    filename = 'add_item.json'
    if path.isfile(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    for i in range(1, len(argv)):
        my_list.append(argv[i])
    save_to_json_file(my_list, filename)

print(add_items())
