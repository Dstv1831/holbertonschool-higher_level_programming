#!/usr/bin/python3

def max_integer(my_list=[]):
    """Find the biggest integer of a list"""
    if len(my_list) == 0:
        return "None"
    else:
        hv = my_list[0]
        for i in my_list:
            if i > hv:
                hv = i
        return hv
