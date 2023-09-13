#!/usr/bin/python3
"""
Check if object is an instance of a class other than int.
"""


def inherits_from(obje, a_class):
    """
    Check if object is an instance of a class
    """
    return isinstance(obje, a_class) and type(obje) != a_class
