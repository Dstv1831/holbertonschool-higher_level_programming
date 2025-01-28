#!/usr/bin/python3

"""
0-square
This module contains the  class square
"""


class Square:
    """
    class square

    attributes:
        size:
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

    def my_print(self):
        """Public instance method that prints a square of the specified size"""
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

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
