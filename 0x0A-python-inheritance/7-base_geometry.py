#!/usr/bin/python3
"""
Module: 7-base_geometry
Contains the BaseGeometry class with public instance methods.
"""


class BaseGeometry:
    """
    A class with public instance methods for geometry operations.
    """

    def area(self):
        """
        Raise an Exception indicating method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer attribute's value.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
