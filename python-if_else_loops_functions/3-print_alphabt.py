#!/usr/bin/python3

""" Write a program that prints the ASCII alphabet,
except for 'e' and 'q', in lowercase, not followed by a new line. """

for n in range(ord('a'), ord('z') + 1):
    if n == ord('q') or n == ord('e'):
        continue
    print("{0}".format(chr(n)), end='')
