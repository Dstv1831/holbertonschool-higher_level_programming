#!/usr/bin/python

def multiply_by_2(a_dictionary):
    """Multiply every item on the dictionary by 2"""
    new_dict = {item : item * 2 for item in a_dictionary}
    return new_dict
