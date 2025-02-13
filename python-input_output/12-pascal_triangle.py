#!/usr/bin/python3

"""
This module contains the pascal_triangle function
"""


def pascal_triangle(n):

    """
    Function that prints the Pascal Triangle
    """

    triangle = [[1]]

    if n <= 0:
        return []

    while len(triangle) != n:
        new = [1]
        pas = triangle[-1]
        for i in range(len(triangle) - 1):
            new.append(pas[i] + pas[i+1])
        new.append(1)
        triangle.append(new)
    return triangle
