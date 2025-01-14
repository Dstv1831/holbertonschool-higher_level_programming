#!/usr/bin/python3

n = 0
while n < 99:
    if 0 <= n < 10:
        n = str(n).zfill(2)
    print("{0}, ".format(n), end='')
    n = int(n)
    n += 1
print("{0}".format(n))
