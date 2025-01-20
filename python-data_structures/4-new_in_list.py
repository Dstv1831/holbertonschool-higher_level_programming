#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    b = my_list.copy()
    if 0 <= idx < len(my_list):
        b[idx] = element
        return b
    else:
        return b
