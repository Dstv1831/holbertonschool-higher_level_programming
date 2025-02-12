#!/usr/bin/python3

"""
This module contains a script that adds all the stdin arguments
to a Python list, and then save them to a file
"""


import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    vector = load_from_json_file("add_item.json")
except FileNotFoundError:
    vector = []
vector = sys.argv
save_to_json_file(vector, "add_item.json")
