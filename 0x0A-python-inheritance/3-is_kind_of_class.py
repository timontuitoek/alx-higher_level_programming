#!/usr/bin/python3
"""
function to check if an object is an instance of a specified class.
"""


def is_kind_of_class(obje, a_class):
    """
    Check if an object is an instance of a specified class or its subclasses.
    """
    return isinstance(obje, a_class)
