#!/usr/bin/python3
"""
The function prints the full name using `first_name` and `last_name`.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints a name using `first_name` and `last_name`.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If `first_name` is not a string.
        TypeError: If `last_name` is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))

