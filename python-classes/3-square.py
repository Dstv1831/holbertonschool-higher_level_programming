#!/usr/bin/python3

"""
3-square
This module contains the class square
"""


class Square:
    """
    class square

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
    