#!/usr/bin/python3

def uppercase(str):

    """ Write a function that prints a string in uppercase followed by a new line. """
    
    for i in str:
        asci = ord(i)
        if 96 < asci < 123:
            i = chr(asci - 32)
        print("{0}".format(i), end = '')
    print()

uppercase("max rocks")
