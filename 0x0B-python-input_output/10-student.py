#!/usr/bin/python3
"""
Retrieve a dictionary representation of a Student instance
"""

class Student:
    """
    student first_name, last_name, age
    """


def __init__(self, first_name, last_name, age):
        """
        Instantiation function for student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self, attrs=None):
            """
            Returns a dictionary representation of an object or
            """

        if attrs is not None and isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
