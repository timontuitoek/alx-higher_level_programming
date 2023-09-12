#!/usr/bin/python3
"""
script defines function that write text file && returns the number of char
"""


def write_file(filename="", text=""):
    """
    write provided text to specified and return number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
