#!/usr/bin/python3

def multiple_return(sentence):
    """Functions that returns a tuple with the length of the string and the first character of it"""
    l= len(sentence)
    if l == 0:
        first_char = 'None'
    else:
        first_char = sentence[0]
    return ((l, first_char))
