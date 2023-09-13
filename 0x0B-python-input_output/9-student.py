#!/usr/bin/python3
"""
Student to JSON
"""


class student:
    """
    class defining a student
    """
    def __init__(self, first_name, last_name, age):
        """
        initializing a student instance with first_name, last_name, and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieve a dictionary representation of a student instance
        """
        return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
