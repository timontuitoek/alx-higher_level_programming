#!/usr/bin/python3
"""
reads file and prints its contents
"""


def read_file(filename=""):
    """
    Replace 'my_file_0.txt' with the actual filename you want to read
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
