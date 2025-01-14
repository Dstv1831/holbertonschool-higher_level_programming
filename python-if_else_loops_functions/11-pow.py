#!/usr/bin/python3

def pow(a, b):
    res = 0
    a = abs(a)
    for i in range (0,b):
        res += a
    if b % 2 != 0:
        res = res * -1
    return (res)

pow(2,2)
