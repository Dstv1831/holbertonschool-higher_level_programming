#!/usr/bin/python3

"""
This module contains a function that returns
the python object from a JSON formated string
"""

import json


def from_json_string(my_str):

    """
    Function returns the Python object
    from a JSON formated string
    """

    json_string = json.loads(my_str)
    return json_string
