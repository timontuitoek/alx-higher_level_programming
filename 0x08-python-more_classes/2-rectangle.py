#!/usr/bin/python3
"""Rectangle empty class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if 0 in (self.__height, self.__width):
            return 0
        return 2 * (self.__height + self.__width)
