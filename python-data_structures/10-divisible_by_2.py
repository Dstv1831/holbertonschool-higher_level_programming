#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Finds all multiples of 2"""
    new_list = ["True" if item % 2 == 0 else "False" for item in my_list]
    return new_list
