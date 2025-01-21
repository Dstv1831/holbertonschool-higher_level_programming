#!/usr/bin/python

def safe_print_list(my_list=[], x=0):
    
    """Function that prints x elements of a list"""
    try:
        list = [my_list[i] for i in range(x)]
    except IndexError:
        list = [item for item in my_list]
    return list
