#!/usr/bin/python3

"""
This module contains a function that
creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):

    """
    Loads a file with a JSON representation
    and creates and Object from it
    """
    with open(file=filename, mode="r", encoding="utf-8") as myfile:
        return (json.load(myfile))
