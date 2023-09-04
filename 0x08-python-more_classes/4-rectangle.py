#!/usr/bin/python3
"""
Rectangle empty class
"""

class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance with optional width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of a rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate and return the perimeter of a rectangle.
        """
        if 0 in (self.__height, self.__width):
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Return a string representation of the rectangle.
        """
        if not self.width or not self.height:
            return ""
        return (("#" * self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        """
        Return a formal string representation of the rectangle.
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

