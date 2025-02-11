#!/usr/bin/python3

"""
This module contains a function that opens a file,
appends a string at the end of it, and returns
the number of characters add it
"""


def append_write(filename="", text=""):

    """
    Function that opens a file,
    appends a string at the end of it,
    and returns the number of characters add it
    """
    with open(file=filename, mode="a", encoding="utf-8") as myfile:
        return myfile.write(text)
