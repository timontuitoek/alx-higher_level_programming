#!/usr/bin/python3
""" Define a Rectangle based on 2-rectangle.py """

class Rectangle:
    """ Define a rectangle with getters and setters """

    def __init__(self, width=0, height=0):
        """ Initialize a new Rectangle instance with optional width and height """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for width """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ Getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for height """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >=0')
        self.__height = value

    def area(self):
        """ Calculate the area of the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Calculate the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ Return the printable representation of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rect = []
            for i in range(self.__height):
                [rect.append('#') for j in range(self.__width)]
                if i != self.__height - 1:
                    rect.append("\n")
            return("".join(rect))

