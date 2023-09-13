#!/usr/bin/python3
"""
Module: 10-square
This module defines a Square class that inherits from Rectangle class.
"""


# Import the Rectangle class from module 9-rectangle
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class representing a geometric square.
    """

    def __init__(self, size):
        """
        Initialize a Square instance with a validated size.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return a string representation of the Square
        """

        return super().__str__()

    def area(self):
        """
        Calculate and return the area of the Square.

        Returns:
            int: The area of the square.
        """

        return self.__size ** 2
