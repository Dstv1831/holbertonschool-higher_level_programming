#!/usr/bin/python3
"""Module that defines a class Square that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a Square using Rectangle."""

    def __init__(self, size):
        """Intialize a new Square.

        Args:
            size (int): The size of the square
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Public instance method that calculates the Area"""
        return pow(self.__size, 2)
