#!/usr/bin/python3

"""
This module contains the pascal_triangle function
"""

def pascal_triangle(n):

    """
    Function that prints the Pascal Triangle
    """

    counter = 0
    pascal = []
    triangle = []

    if n <= 0:
        return triangle
        
    while counter != n:
        pascal = [1]
        for count in enumerate(pascal):
            pascal.append(pascal[count] + pascal[count + 1])
            print(pascal)
        counter += 1
    