#!/usr/bin/python3

"""
3-say_my_name

This module provides a function to print the first and last name arguments

"""


def say_my_name(first_name, last_name=""):
    """
    Prints a sentence with both arguments firs and last name.

    Raises:
    TypeError: If either first or last name are non-strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
       