#!usr/bin/python

"""
4-print_square.py

This module provides a function that prints a square of the size of its argument

"""


def print_square(size):
    """
    Prints a square with dimensions 'size'.

    Raises:
    TypeError: If the argument is not an integer or is below 0.
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range (size):
        for j in range (size):
            print("#", end='')
