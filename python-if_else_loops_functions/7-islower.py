#!/usr/bin/python3

""" Write a function that checks for lowercase character."""

def islower(c):
    if 60 < ord(c) < 123:
        print("{0} is lower".format(c))
        return (True)
    else:
        print("{0} is upper".format(c))
        return (False)
