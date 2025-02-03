#!/usr/bin/python3

"""This module contains a function that chcks for types of same class"""


def is_same_class(obj, a_class):
    """Function that returns True if the object
    is exactly an instance (Type) of the specified class;
    otherwise False."""

    if type(obj) is a_class:
        return True
    else:
        return False
