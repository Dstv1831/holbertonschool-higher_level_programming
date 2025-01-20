#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Deletes the item at the idx position"""
    if 0 <= idx < len(my_list):
        del my_list[idx]
        return my_list
    else:
        return my_list
