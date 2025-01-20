#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer"""
    new_list = set(my_list)
    total = sum(new_list)
    return total
 