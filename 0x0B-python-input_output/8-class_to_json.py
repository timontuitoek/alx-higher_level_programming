#!/usr/bin/python3
"""
Class to JSON
"""


def class_to_json(obj):
    """
    converting an object to a serializable dictionary
    """
    return obj.__dict__
