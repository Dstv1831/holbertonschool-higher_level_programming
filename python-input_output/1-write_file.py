#!/usr/bin/python3

"""
This module contains a function that opens a file
writes a string on it and returns the number
of characters on it
"""


def write_file(filename = "", text = ""):

    """
    Function that opens a file, writes on 
    it and print the number of characters
    """

    with open(file = filename, mode = "w", encoding = "utf-8") as myfile:
        myfile.write(text)
        content_list = (myfile.read()).split

    counter = 0
    for words in content_list:
        for character in words:
            counter += 1
    
    return counter