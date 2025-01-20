#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Printing a Matrix of integeres"""
    for i in matrix:
        for j in range (3):
            print("{:d}".format(i[j]), end =' ')
        print()
            