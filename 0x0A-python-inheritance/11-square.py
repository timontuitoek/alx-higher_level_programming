#!/usr/bin/python3
"""
Module: 11-square
This module defines a Square class that inherits from Rectangle class.
"""


# Import the Rectangle class from module 9-rectangle
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class representing a geometric square.

    Attributes:
        __size (int): The size of the square's sides.
    """

    def __init__(self, size):
        """
        Initialize a Square instance with a validated size.

        Args:
            size (int): The size of the square's sides.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return a string representation of the Square.

        Returns:
            str: A formatted string containing the size.
        """

        return("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """
        Calculate and return the area of the Square.

        Returns:
            int: The area of the square.
        """

        return self.__size ** 2
