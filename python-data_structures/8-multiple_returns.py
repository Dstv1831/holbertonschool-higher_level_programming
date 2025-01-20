#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple with the stirng length and its first character"""
    long = len(sentence)
    if long == 0:
        first_char = 'None'
    else:
        first_char = sentence[0]
    return (long, first_char)
