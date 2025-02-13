#!/usr/bin/python3

"""
This module contains a Class Student with a public
method that retrieves a dictionary representation
of a student instance and the specified attributes
"""


class Student:
    """
    Class that creates a student

    attributes:
        public instance first_name
        public instance last_name
        public instance age
    
    public methods:
        to_jason: Return the specified attributes value 
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None): 
        if attr:
            new_dict = self.__dict__
            for each in attr:
                new_dict.update(new_dict[each])
            return new_dict            

        else:
            return self.__dict__
