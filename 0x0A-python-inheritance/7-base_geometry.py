#!/usr/bin/python3
"""
Module: 7-base_geometry
Contains the BaseGeometry class with public instance methods.
"""

class BaseGeometry:
    """
    A class with public instance methods for geometry operations.

    Methods:
        - area(self): Raises an Exception with the message 'area() is not implemented'.
        - integer_validator(self, name, value): Validates the value for an integer attribute.
    """

    def area(self):
        """
        Raise an Exception indicating that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validate an integer attribute's value.

        Args:
            name (str): The name of the attribute.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

