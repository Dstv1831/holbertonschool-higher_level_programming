#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list

# In Python's ternary expression syntax:
# (value_if_true) if condition else (value_if_false)