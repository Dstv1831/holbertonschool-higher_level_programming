#!/usr/bin/python3

"""
Module that serializes a Python dictionary
to a JSON file and deserialize the JSON file 
to recreate the Python Dictionary.
"""
import json


def serialize_and_save_to_file(data, filename):

    with open(file=filename, mode="w", encoding="utf-8") as myfile:
        return json.dump(data, myfile)


def load_and_deserialize(filename):

    with open(file=filename, mode="w", encoding="utf-8") as myfile:
        return json.load(myfile)
