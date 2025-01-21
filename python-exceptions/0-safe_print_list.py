#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    """Function that prints x elements of a list"""

    try:
        for i in range(x):
            print('{}'.format(my_list[i]), end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
