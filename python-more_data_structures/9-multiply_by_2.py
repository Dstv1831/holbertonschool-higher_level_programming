#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Multiply every item on the dictionary by 2"""
    new_dict = {k: v * 2 for (k, v) in a_dictionary.items()}
    return new_dict
