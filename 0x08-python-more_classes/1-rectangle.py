#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle object with optional width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.
        """
        if not isinstance(value, int):
            """
            Check if the value is an integer; if not, raise a TypeError.
            """
            raise TypeError("width must be an integer")
        if value < 0:
            """
            Check if the value is non-negative; if not, raise a ValueError.
            """
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.
        """
        if not isinstance(value, int):
            """
            Check if the value is an integer; if not, raise a TypeError.
            """
            raise TypeError("height must be an integer")
        if value < 0:
            """
            Check if the value is non-negative; if not, raise a ValueError.
            """
            raise ValueError("height must be >= 0")
        self.__height = value

