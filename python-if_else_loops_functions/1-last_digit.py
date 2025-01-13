#!/usr/bin/python3
import random


def printing(n, ld, txt):
    print(f"Last digit of {n} is {ld} {txt}")


number = random.randint(-10000, 10000)

if number > 0:
    ld = number % 10
else:
    ld = abs(number) % 10 * -1
# YOUR CODE HERE
if ld > 5:
    text = "and is greater than 5"
elif ld == 0:
    text = "and is 0"
else:
    text = "and is less than 6 and not 0"

printing(number, ld, text)
