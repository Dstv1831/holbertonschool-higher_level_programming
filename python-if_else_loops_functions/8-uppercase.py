#!/usr/bin/python3

def uppercase(str):

    """ Write a function that prints a string in uppercase followed by a new line. """
    
    for i in str:
        if (ord(i) > 96 and ord(i) < 123):
            i = chr(ord(i) - 32)
        print('{0}'.format(i), end="")
    print("")
