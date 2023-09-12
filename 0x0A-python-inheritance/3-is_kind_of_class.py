#!/usr/bin/python3
"""
This script defines a function to check if an object is an instance of, or inherits from, a specified class.
"""

def is_kind_of_class(obje, a_class):
    """
    Check if an object is an instance of a specified class or its subclasses.

    Args:
        obje: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if obje is an instance of a_class or its subclasses, False otherwise.
    """
    return isinstance(obje, a_class)

