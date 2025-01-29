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
        
    @property
    def width(self):
        """Getter decorator"""
        return self.width
    
    @width.setter
    def width(self, w):
        """Setter decorator"""
        if not isinstance(w, int):
            raise TypeError("width must be an integer")
        elif w < 0:
            raise ValueError("width must be >= 0")
        self.width = w
    
    @property
    def height(self):
        """Getter decorator"""
        return self.height
        
    @height.setter
    def height(self, h):
        """Setter decorator"""
        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        elif h < 0:
            raise ValueError("height must be >= 0")
        self.height = h
