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

    def __init__(self, width: int, height: int):
        """
        Initialize the Rectangle instance with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self) -> int:
        """
        Calculate and return the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self) -> str:
        """
        Return a string representation of the Rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
