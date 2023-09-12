#!/usr/bin/python3
"""
Save object to a file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Serialize given object to JSON representation and save it to text file
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file, ensure_ascii=False, indent=4)
