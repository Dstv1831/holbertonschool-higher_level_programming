#!/usr/bin/python3

""" Write a function that checks for lowercase character."""


def islower(c):
    if 96 < ord(c) < 123:
        return (True)
    else:
        return (False)
