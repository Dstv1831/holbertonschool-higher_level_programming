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
        instantion with optional values

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter decorator"""
        return self.__width

    @width.setter
    def width(self, w):
        """Setter decorator"""
        if not isinstance(w, int):
            raise TypeError("width must be an integer")
        elif w < 0:
            raise ValueError("width must be >= 0")
        self.__width = w

    @property
    def height(self):
        """Getter decorator"""
        return self.__height

    @height.setter
    def height(self, h):
        """Setter decorator"""
        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        elif h < 0:
            raise ValueError("height must be >= 0")
        self.__height = h

    def area(self):
        """public method that return the area"""
        return (self.height * self.width)

    def perimeter(self):
        """Public method that return the area"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.height + self.width) * 2)

    def __str__(self):
        """Print the rectangle by using the method str  """
        if self.width == 0 or self.height == 0:
            return ("")
        rect = []
        for i in range(self.height):
            [rect.append(str(self.print_symbol) * self.width)]
        return ("\n".join(rect))

    def __repr__(self):
        """Print the string representation of a new instance"""
        string = repr(f"Rectangle({self.width}, {self.height})")
        string = eval(string)
        return string

    def __del__(self):
        """Delete the rectangle instance """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that returns the
        biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_2.area() > rect_1.area()):
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """class method that returns a new Rectangle instance"""
        return (cls(width=size, height=size))
