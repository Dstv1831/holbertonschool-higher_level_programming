#!/usr/bin/python3

"""Module containing an empty class"""


class BaseGeometry:
    """Empty class BaseGeometry that inherits from list"""

    def area(self):
        """Public instance method that calculates the Area"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Public instance method that validates """
        if not type(value) is int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
         
