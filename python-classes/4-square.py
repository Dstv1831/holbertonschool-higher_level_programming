#!/usr/bin/python3

"""
0-square
This module contains the  class square
"""


class Square:
    """
    class square with decorators getter and setter

    attributes:
        size: size of the square
    
    methods:
        area: Calculates the area of the square
    """
    def __init__(self, size=0):
        """Private instance attribue with optional size value initialized """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Public instance method that calculates the area"""
        return pow(self.__size, 2)

    """Decorator for a getter"""
    @property
    def size(self):
        return self.__size

    """Decorator for a setter to adjust the value of an attribute"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
