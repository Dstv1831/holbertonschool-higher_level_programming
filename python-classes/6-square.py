#!/usr/bin/python3

"""
5-square
This module contains the class square
"""


class Square:
    """
    class square with decorators getter and setter

    attributes:
        size (int): The size of the new square.
        position (int, int): The position of the new square.

    methods:
        area: Calculates the area of the square
        my_print: Prints the square in the stdout
    """
    def __init__(self, size=0, position=(0, 0)):
        """Private instance attribue with optional size value initialized """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Decorator for a getter size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Decorator for a setter to adjust the value of the size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Decorator for a getter position"""
        return self.__position

    @position.setter
    def position(self, coordinates):
        """Decorator for a setter to adjust the value
        of the position attribute"""

        if (not isinstance(coordinates, tuple)
                or len(coordinates) != 2
                or not all(isinstance(coord, int) for coord in coordinates)
                or not all((coord >= 0) for coord in coordinates)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = coordinates

    def area(self):
        """Public instance method that calculates the area"""
        return pow(self.__size, 2)

    def my_print(self):
        """Public instance method that prints a square of the specified size"""
        if (self.__size == 0):
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
