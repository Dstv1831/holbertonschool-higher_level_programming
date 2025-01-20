#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Deletes the item at the idx position"""
    new_list = []
    if 0 <= idx < len(my_list):
        del new_list[idx]
        return new_list
    else:
        return my_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)