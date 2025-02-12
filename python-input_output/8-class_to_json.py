#!/usr/bin/python3

"""
This module contains a function that returns the
dictionary description of a simple data structure
for JSON serialization of an object
"""


def class_to_json(obj):
    
    """
    returns de dictionary description of a class
    """
    return obj.__dict__
