#!/usr/bin/python3
"""
Class to JSON
"""


def class_to_json(obj):
    """
    converting an object to a serializable dictionary
    """
    if not hasattr(obj, '__dict__'):
        raise valuerror("object must be an instance of a class")

    serializable_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value

            return serializable_dict
