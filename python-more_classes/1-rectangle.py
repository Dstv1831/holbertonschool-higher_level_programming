#!/usr/bin/python3
"""
0-rectangle
This module contains the empty class rectangle
"""


class Rectangle:
    """
    Empty class that creates a rectangle 
    
    attirbutes:
        private instance width
        private instance heigh

    """

    def __init__(self, width='0', height = '0'):
        self.width = width
        self.height = height
        
    """Getter decorator"""
    @property
    def width(self):
        return self.width
    
    """Setter decorator"""
    @width.setter
    def width(self, w):
        if not isinstance(w, int):
            raise TypeError("width must be an integer")
        elif w < 0:
            raise ValueError("width must be >= 0")
        self.width = w
    
    
    """Getter decorator"""
    @property
    def height(self):
        return self.height
    
    """Setter decorator"""
    @height.setter
    def height(self, h):
        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        elif h < 0:
            raise ValueError("height must be >= 0")
        self.height = h
