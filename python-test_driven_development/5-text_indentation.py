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
    while i < len(text):
        if text[i] in '.?:':
            print(text[i], end='')
            print('\n')
            while (i + 1 < len(text) and text[i + 1] == ' '):
                i += 1
        else:
            print(text[i], end='')
        i += 1
