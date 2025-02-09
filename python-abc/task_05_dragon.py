#!/usr/bin/python3

""" Module that contains the "Dragon" Class, which
    inherits from two mixin classes 
    "SwimMixin" & "FlyMixin"
"""
class SwimMixin:
    
    def swim(self):
        return print("The creature swims!")
    
class FlyMixin:
    
    def fly(self):
        return print("The creature flies!")

    
class Dragon(SwimMixin, FlyMixin):
    
    """
    Class Dragon that inherits from both
    a SwimMixin and a FlyMixin class. 

    Attributes:
        Name: name of the new object of class Dragon 
    Methods:
        Roar: Returns "<name> roars!"
    """ 

    def __init__(self):
        self.name = "Raehgar"
    
    def roar(self):
        print(f"The dragon roars!")