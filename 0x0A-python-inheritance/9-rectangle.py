#!/usr/bin/python3
"""
Module: 8-rectangle
This module defines a Rectangle class that inherits from BaseGeometry.
"""


# Import the BaseGeometry class from module 7-base_geometry
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class representing a geometric rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Return a string representation of the Rectangle.

        Returns:
            str: A formatted string containing width and height.
        """

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """
        Calculate and return the area of the Rectangle.
        """

        return self.__width * self.__height
