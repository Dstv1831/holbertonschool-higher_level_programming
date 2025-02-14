#!/usr/bin/python3

"""
Module that serialize and deserialize a 
custom Python object using the pickle module
"""

import pickle

class CustomObject:
    
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        print (f"Name: {self.name}"
               f"Age:{self.age}"
               f"Is Student:{self.is_student}")
        
    def serialize(self, filename):
        with open(file=filename, mode="w", encoding="utf-8") as myfile:
            pickle.dump(self, myfile)


    @classmethod
    def deserialize(cls, filename):
        with open(file=filename, mode="r", encoding="utf-8") as myfile:
            data = pickle.load(myfile)
            return data
