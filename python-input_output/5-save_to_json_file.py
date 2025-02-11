#!/usr/bin/python3

"""
This module contains a function that writes
an Object to a text file, using JSON representation
"""

import json

def save_to_json_file(my_obj, filename):

    """
    writes an Object to a text file, using a JSON representation
    """
    json_encoded = json.dumps(my_obj)
    with open(file=filename,mode="w",encoding="utf-8") as myfile:
        myfile.write(json_encoded)
    return 0
