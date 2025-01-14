#!/usr/bin/python3

u = 0
while u < 8:
    for d in range(0,10):
        if u == d or u > d :
            continue
        print("{0}{1}, ".format(u, d), end="")
    u += 1
print("{0}{1}".format(u, d), end="")

