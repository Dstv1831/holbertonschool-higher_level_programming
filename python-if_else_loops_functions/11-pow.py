#!/usr/bin/python3

def pow(a, b):
    
    res = 1
    for i in range(0, abs(b)):
        res = res * a
    if b < 0:
        res = 1/res
    return (res)
