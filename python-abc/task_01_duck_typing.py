#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi

""" Module that contains an Abstract Base Class (ABCs)
    classes that are meant to be incomplete
    "Animal" and two derived subclasses "Dog" & "Cat" 
"""


class Shape(ABC):
    """
    Abstrac class named Animal with the ABC package

    Methods:
    sound
    """

    @abstractmethod
    def area(self):
        """ Abstrac method: Declare but not defined"""
        pass

    @abstractmethod
    def perimeter(self):
        """ Abstrac method: Declare but not defined"""
        pass

class Rectangle(Shape):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return (self.height * self.width)

    def perimeter(self):
        return (self.height * 2 + 2 * self.width)


class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (pi)*pow(self.radius, 2)

    def perimeter(self):
        return (abs(2*pi*self.radius))

def shape_info(figure):
    """Function that takes an object as an argument"""
    print(f"Area: {figure.area()}")
    print(f"Perimeter: {figure.perimeter()}")
    return 0
