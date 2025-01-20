#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Printing a matrix of integers"""
    for row in matrix:
        for j, value in enumerate(row):
            print("{:d}".format(value), end='')
            if j != len(row) - 1:
                print(" ", end='')
        print()