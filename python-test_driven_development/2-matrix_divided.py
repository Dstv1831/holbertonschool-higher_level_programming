#!/usr/bin/python3

"""
2-matrix_divided.py

This module provides a function to divide all elements of a matrix

"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    details:
        [num for row in matrix for num in row] means:
        for each row on matrix (outer loop)
        for each num on row (inner loop)
        value will be num 
    """
    if not isinstance(matrix, list) or matrix == [] or not all(isinstance(row, list) for row in matrix) or not all((isinstance(ele, int) or isinstance(ele, float)) for ele in [num for row in matrix for num in row]):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all([len(row) == len(matrix[0]) for row in matrix]):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not (matrix or div):
        raise ValueError("Missing 1 or 2 arguments")
    """ The lambda method is necessary to keep the return a matrix structure"""
    return ([list(map(lambda x: round(x/div, 2), row)) for row in matrix])
