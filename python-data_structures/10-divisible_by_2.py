#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = ("True" for item in my_list if item % 2 == 0 )
    return new_list

my_list = [0, 1, 2, 3, 4, 5, 6]
print(divisible_by_2(my_list))
