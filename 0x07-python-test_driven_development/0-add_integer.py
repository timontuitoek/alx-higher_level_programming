#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer or float. Default is 98.

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is neither an integer nor a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    a = int(a)
    
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    b = int(b)
    
    return a + b

