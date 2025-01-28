# #!/usr/bin/python3

# """
# 5-square
# This module contains the class square
# """


# class Square:
#     """
#     class square with decorators getter and setter

#     attributes:
#         size (int): The size of the new square.
#         position (int, int): The position of the new square.
    
#     methods:
#         area: Calculates the area of the square
#         my_print: Prints the square in the stdout
#     """
#     def __init__(self, size=0, position=(0, 0)):
#         """Private instance attribue with optional size value initialized """
#         if not isinstance(size, int):
#             raise TypeError("size must be an integer")
#         elif size < 0:
#             raise TypeError("size must be >= 0")
#         else:
#             self.__size = size

#         if (not isinstance(position, tuple) or 
#             not all(isinstance(coord, int) for coord in position) or 
#             not all((coord >= 0) for coord in position)):
#             raise TypeError("position must be a tuple of 2 positive integers")
#         else:
#             self.__position = position

#         self.__size = size
#         self.__position = position

#     @property
#     def size(self):
#         """Decorator for a getter size"""
#         return self.__size
    
#     @property
#     def position(self):
#         """Decorator for a getter position"""
#         return self.__position

#     @size.setter
#     def size(self, value):
#         """Decorator for a setter to adjust the value of the size attribute"""
#         if not isinstance(value, int):
#             raise TypeError("size must be an integer")
#         elif value < 0:
#             raise ValueError("size must be >= 0")
#         else:
#             self.__size = value

#     @position.setter
#     def position(self, coordinates):
#         """Decorator for a setter to adjust the value of the position attribute"""
#         if (not isinstance(coordinates, tuple) or 
#             not all(isinstance(coord, int) for coord in coordinates) or 
#             not all((coord >= 0) for coord in coordinates)):
#             raise TypeError("position must be a tuple of 2 positive integers")
#         else:
#             self.__position = coordinates

#     def area(self):
#         """Public instance method that calculates the area"""
#         return pow(self.__size, 2)

#     def my_print(self):
#         """Public instance method that prints a square of the specified size"""
#         if (self.__size == 0):
#             print()
#         else:
#             for y in range(self.__position[1]):
#                     print()
#             for i in range(self.__size):
#                 for x in range(self.__position[0]):
#                     print(' ', end="")
#                 for j in range(self.__size):
#                     print("#", end="")
#                 print()

#!/usr/bin/python3
# 6-square.py
# Brennan D Baraban <375@holbertonschool.com>
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
