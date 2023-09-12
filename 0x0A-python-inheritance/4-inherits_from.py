#!/usr/bin/python3
"""Module 4-inherits_from.py
Check if the object is an instance of a class other than int or the object class.
"""

def inherits_from(obje, a_class):
    """
    Check if the object is an instance of a class that inherits from a specified class.

    Args:
        obje: The object to be evaluated.
        a_class: The class to evaluate against.
        
    Returns:
        True if obje is an instance of a subclass of a_class, False otherwise.
    """
    return isinstance(obje, a_class) and type(obje) != a_class

