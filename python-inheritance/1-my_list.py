#!/usr/bin/python3

"""Class that inherist from the object list"""

class MyList(list):
    """MyList that inherits from list"""

    def print_sorted(self):
        """Public instance Method that prints the list but sorted"""
        return print(sorted(self))
