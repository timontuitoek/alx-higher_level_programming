#!/usr/bin/python3
"""
Module: 8-rectangle
"""

# Import the BaseGeometry class from module 7-base_geometry
from typing import Union
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Class Rectangle inherits from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width: int, height: int):
        """
        Initialize the Rectangle instance with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Validate and set the width and height using integer_validator method from BaseGeometry
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self) -> int:
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self) -> str:
        """
        Return a string representation of the Rectangle.

        Returns:
            str: A string representation of the Rectangle instance.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

