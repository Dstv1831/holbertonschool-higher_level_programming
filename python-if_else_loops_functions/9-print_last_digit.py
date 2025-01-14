#!/usr/bin/python3

def print_last_digit(number):
    """ Write a function that prints the last digit of a number. """
    if number > 0:
        ld = number % 10
    else:
        ld = abs(number) % 10 * -1
    print(ld, end='')
    return(ld)
