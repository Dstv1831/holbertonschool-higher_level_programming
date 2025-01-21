#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Create a new list with all its value multiply by a number"""
    return list(map(lambda x: x*number, my_list))
