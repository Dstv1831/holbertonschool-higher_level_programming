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

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return (self.length * self.width)

    def perimeter(self):
        return (self.length * 2 + 2 * self.width)


class Circle(Shape):
    
    def __init__(self, radius ):
        self.radius = radius

    def area(self):
        return (pi)*pow(self.radius, 2)

    def perimeter(self):
        return (2*pi*self.radius)
