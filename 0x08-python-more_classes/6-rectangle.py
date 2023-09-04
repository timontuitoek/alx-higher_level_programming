#!/usr/bin/python3
"""
Defining a rectangle based on 4-rectangle.py
"""

class Rectangle:
    """
    String representation of a rectangle
    """

    number_of_instances = 0  # Class variable to count the number of instances

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance with optional width and height.
        Increase the number of instances by 1.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        self.__width = value
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
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
        self.__height = value
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >=0')
        self.__height = value

    def area(self):
        """
        Calculate and return the area of a rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculate and return the perimeter of a rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        Return a string representation of the rectangle.
        """
        total = ""
        if self.__height == 0 or self.__width == 0:
            return total
        for i in range(self.__height):
            total += ("#" * self.__width)
            if i is not self.__height - 1:
                total += "\n"
        return total

    def __repr__(self):
        """
        Return a formal string representation of the rectangle.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor method to print a message when deleting a rectangle instance.
        Decrease the number of instances by 1.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

