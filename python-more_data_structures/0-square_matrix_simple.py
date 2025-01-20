#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    
    """Calculates the square of each item inside a matrix"""

    new_matrix = [[item ** 2 for item in row] for row in matrix]
    #Nested list comprehension 
    return new_matrix
