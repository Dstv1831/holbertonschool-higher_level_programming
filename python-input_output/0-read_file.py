#!/usr/bin/python3

"""
This module contains a function that opens a file
reads and print its content in stdout
"""

def read_file(filename=""):

    "Function that opens a file and print its content into stdout"

    with open(file=filename, encoding="utf-8") as myfile:
        print(myfile.read())
