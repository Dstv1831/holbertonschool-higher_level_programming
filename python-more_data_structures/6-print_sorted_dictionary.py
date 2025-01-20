#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys."""
    [print("{}: {}".format(items, a_dictionary[items])) for items in sorted(a_dictionary)]
