#!/usr/bin/python3
"""
Defines a matrix division function.
"""

def matrix_divided(matrix, divisor):
    """
    Divide all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): A matrix containing integers or floats.
        divisor (int or float): The divisor for the division.

    Returns:
        list of lists: A new matrix representing the result of the division.
        
    Raises:
        TypeError: If matrix is not a valid matrix or contains non-numeric elements.
        TypeError: If divisor is not a number (int or float).
        ZeroDivisionError: If divisor is 0.

    Example:
        matrix_divided([[1, 2, 3], [4, 5, 6]], 2) returns [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
    """
    """ Validate the matrix """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must contain only integers or floats")
    
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("all rows in the matrix must have the same size")

    """ Validate the divisor """
    if not isinstance(divisor, (int, float)):
        raise TypeError("divisor must be a number")
    
    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    """ Perform the division and round the result to 2 decimal places """
    result = [[round(num / divisor, 2) for num in row] for row in matrix]

    return result

