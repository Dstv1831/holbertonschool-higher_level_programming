#!/usr/bin/python3
from abc import ABC, abstractmethod

""" Module that contains an Abstract Base Class (ABCs)
    classes that are meant to be incomplete
    "Animal" and two derived subclasses "Dog" & "Cat" 
"""


class Animal(ABC):
    """
    Abstrac class named Animal with the ABC package

    Methods:
    sound
    """

    @abstractmethod
    def sound(self):
        """ Abstrac method: Declare but not defined"""
        pass

class Dog(Animal):

    dog_sound = "Bark"

    def sound(self):
        return f"{self.dog_sound}"

class Cat(Animal):

    dog_sound = "Meow"

    def sound(self):
        return f"{self.dog_sound}"
