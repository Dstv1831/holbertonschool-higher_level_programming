#!/usr/bin/python3

def uppercase(str):
    """ Write a function that prints a string in uppercase followed by a new line. """
    for i in str:
        asci = ord(i)
        if 96 < asci < 123:
            new_char = chr(asci - 32)
            print(new_char, end = '')
        else:
            print(i, end = '')

