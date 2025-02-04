#!/usr/bin/python3
"""Module that defines a class Rectangle that inherits from BaseGeometry."""

Base_Geo = __import__('7-base_geometry').BaseGeometry


class Rectangle(Base_Geo):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Public instance method that calculates the Area"""
        return (self.__width*self.__height)

    def __str__(self):
        """str method, human-readable, or informal,
        string representation of an object."""
        return (f"[Rectangle] {self.__width}/{self.__height}")
