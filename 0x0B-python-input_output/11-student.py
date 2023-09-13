#!/usr/bin/python3
"""
Student to disk and reload
"""


class Student:
    """
    Defining student first_name, last_name and age
    """
def __init__(self, first_name, last_name, age):

    self.first_name = first_name
    self.last_name = last_name
    self.age = age

    def to_json(self, attrs=None):
        """
        Rtrieves a dictionary representation of a Student instance.
        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        """
        for key, value in json.items():
            setattr(self, key, value)
