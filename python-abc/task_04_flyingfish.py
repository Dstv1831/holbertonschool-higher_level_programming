#!/usr/bin/python3

""" Module that contains the FlyingFish class which inherits
    from two different classes "Bird" & "Fish"
"""
class Bird:
    
    def fly(self):
        return print("The bird is flying")

    def habitat(self):
        return print("The bird lives in the sky")

class Fish:

    def swim(self):
        return print("The fish is swimming")

    def habitat(self):
        return print("The fish lives in water")
    
class FlyingFish(Fish, Bird):
    
    """
    Class FlyingFish that inherits from both
    a Fish class and a Bird class. Within FlyingFish,
    override methods from both parents 

    Methods:
        Fly: Returns "The flying fish is soaring!"
        Swim: Returns "The flying fish is swimming!"
        Habitat: Returns "The flying fish lives both in water and the sky!"
    """ 

    def fly(self):
        return print("The flying fish is soaring!")
    
    def swim(self):
        return print("The flying fish is swimming!")

    def habitat(self):
        return print("The flying fish lives both in water and the sky!")