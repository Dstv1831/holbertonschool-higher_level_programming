#!/usr/bin/python3

"""
This module contains a Class Student with a public 
method that retrieves a dictionary representation
of a student instance
"""

class Student:
    
    """
    Class that creates a student

    attirbutes:
        public instance first_name
        public instance last_name
        public instance age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
