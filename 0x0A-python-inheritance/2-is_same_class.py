#!/usr/bin/python3
"""same_class"""

def is_same_class(obje, a_class):
    """
        Returns True if obje is exactly an instance of a_class; otherwise False
    """
    return type(obje) is a_class
