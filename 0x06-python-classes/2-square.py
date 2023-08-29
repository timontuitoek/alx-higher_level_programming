class Square:
    def __init__(self, size=0):
        # Constructor method for the Square class.
        # Initializes an instance of Square with a given size.
        
        # Check if the provided size is an integer.
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        
        # Check if the provided size is a non-negative value.
        elif size < 0:
            raise ValueError("size must be >= 0")
        
        # If both checks pass, initialize the __size attribute.
        else:
            self.__size = size

