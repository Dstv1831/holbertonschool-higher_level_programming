#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple with the stirng length and its first character"""
    l = len(sentence)
    if l == 0:
        first_char = 'None'
    else:
        first_char = sentence[0]
    return (l, first_char)
