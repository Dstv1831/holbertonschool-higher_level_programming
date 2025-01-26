#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    while(text):
        i = 0
        print(text[i])
        i += 1

text_indentation("Konbanwa david san")