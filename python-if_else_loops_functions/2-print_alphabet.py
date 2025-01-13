#!/usr/bin/python3

"""Print the alphabet in lowercase, not followed by a new line."""

for n in range (ord('a'),ord('z') + 1):
    print("{0}".format(chr(n)), end='')
    