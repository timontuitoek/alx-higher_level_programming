#!/usr/bin/python3
"""
class that inherits from list
sort in (ascending sort)
"""

class MyList(list):
    """
    A function that print the list in sorted ascending order
    """
    def print_sorted(self):
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
