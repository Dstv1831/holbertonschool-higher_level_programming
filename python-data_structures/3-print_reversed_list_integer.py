#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints the elements of a list in reverse"""
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
