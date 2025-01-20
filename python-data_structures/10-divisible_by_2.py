#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = ("True" if item % 2 == 0 else "False" for item in my_list)
    return new_list

my_list = [0, 1, 2, 3, 4, 5, 6]
print(divisible_by_2(my_list))
