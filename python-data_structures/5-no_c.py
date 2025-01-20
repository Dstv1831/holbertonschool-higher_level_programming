#!/usr/bin/python3

def no_c(my_string):
    """Eliminates the C character in a string"""
    for i in my_string:
        if i == 'c':
            continue
        print(i, end='')
    print()
