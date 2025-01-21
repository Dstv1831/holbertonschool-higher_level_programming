#!/usr/bin/python3

def best_score(a_dictionary):

    """Find the highest score in a dcitionary"""

    if len(a_dictionary) != 0:
        max_val = max(a_dictionary.values())
        return max_val
    else:
        return "none"
