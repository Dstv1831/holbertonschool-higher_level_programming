#!/usr/bin/python3

"""
This module contains a function that returns
the JSON formatted string representation of an object
(ENCODING)
"""

import json


def to_json_string(my_obj):

    """
    Function returns the JSON
    representation of an object
    """

    json_string = json.dumps(my_obj)
    return json_string
