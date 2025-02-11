#!/usr/bin/python3
import json

"""
This module contains a function that returns
the JSON representation of an object
"""


def to_json_string(my_obj):

    """
    Function returns the JSON 
    representation of an object
    """

    json_string = json.dumps(my_obj)
    return json_string
    
