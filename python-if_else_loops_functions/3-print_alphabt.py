#!/usr/bin/python3

for n in range(ord('a'), ord('z') + 1):
    if n == ord('q') or n == ord('e'):
        continue
    print("{0}".format(chr(n)), end='')
