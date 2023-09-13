#!/usr/bin/python3
"""
Module: 8-rectangle
"""


from typing import Union
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        inheritance function
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
