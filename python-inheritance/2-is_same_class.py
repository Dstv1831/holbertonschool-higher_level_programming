#!/usr/bin/python3

"""This module contains a function that chcks for instances of same classs"""


def is_kind_of_class(obj, a_class):
    """Function that returns True if the object
    is exactly an instance of the specified class;
    otherwise False."""

    if isinstance(obj, a_class):
        return True
    else:
        return False
