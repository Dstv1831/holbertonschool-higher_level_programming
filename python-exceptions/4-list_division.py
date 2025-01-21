#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
        result = None
    try:
        result = a // b
        return float(result)
    except ZeroDivisionError:
        return "None"
    finally:
        if result is None:
            print("Inside result: {}".format("None"))
        else:
            print("Inside result: {:0.1f}".format(result))