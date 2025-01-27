#!/usr/bin/python3

class square():

    """
    Class that defines a square

    Attributes:
        size: private instance 
    
    """

    def __init__(self, heigh):
        self.height = heigh

    @property
    def height(self):
        return self.__height