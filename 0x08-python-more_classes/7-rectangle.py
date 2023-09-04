#!/usr/bin/python3
"""
Rectangle empty class
"""

class Rectangle:
    """
    Rectangle class
    """

    number_of_instances = 0  # Class variable to count the number of instances
    print_symbol = "#"      # Class variable for the symbol used in printing

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance with optional width and height.
        Increase the number of instances by 1.
        """
        self.width = width
        self.height = height
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
        return ((str(self.print_symbol) *
                 self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        """
        Return a formal string representation of the rectangle.
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """
        Destructor method to print a message when deleting a rectangle instance.
        Decrease the number of instances by 1.
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

