#!/usr/bin/python3

""" Module contains a function that checks if an object
is an instance of a class that inherited 
(directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """Function that returns True if the object
    is exactly an instance of the specified class;
    otherwise False."""

    if issubclass((type(obj).__name__), a_class):
        return True
    else:
        return False
