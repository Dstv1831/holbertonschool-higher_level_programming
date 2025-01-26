#!/usr/bin/python3
"""
5-text_indentation.py

This module provides a function that prints a text
with two new lines after encountering the characters:
":", ".", "?" 
"""


def text_indentation(text):
    """
    Prints a text with a new line indented 
    if any of the characters ":", ".", "?" is found

    Raises:
    TypeError: If the argument is not a string
    """
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    while(i < len(text)):
        if text[i] != '.' and text[i] != '?' and text[i] !=':':
            print(text[i], end='')
        else:
            print(text[i])
            print('\n')
        i += 1
