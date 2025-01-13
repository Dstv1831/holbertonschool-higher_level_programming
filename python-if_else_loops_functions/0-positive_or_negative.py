#!/usr/bin/python3
import random

def printing (n, text):
    print(f"{n} {text}")

number = random.randint(-10, 10)
if number > 0 :
    text = "is positive"
elif number < 0 :
    text = "is negative"
else:
    text = "is zero"
printing(number, text)
    