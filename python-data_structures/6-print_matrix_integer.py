#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Printing a Matrix of integeres"""
    l = len(matrix)
    for i in matrix:
        for j in range (l):
                print("{:d}".format(i[j]), end ='')
                if j != (l):
                     print(" ", end='')
        print()
            