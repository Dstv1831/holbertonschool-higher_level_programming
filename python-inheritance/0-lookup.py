#!/usr/bin/python3

def lookup(obj):
    """Function that returns a list of all
    available attirbutes and methods of an object"""
    return (obj.__dir__())
