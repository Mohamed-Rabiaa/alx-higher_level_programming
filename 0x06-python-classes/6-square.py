#!/usr/bin/python3
""" This module defines the class 'Square' """


class Square:
    """ Creating a class named 'Square' with a private
    instance attribute size. """

    def __init__(self, size=0, position=(0, 0)):
        """ initializing the size and position attributes
        and checking if the size is an integer
        and if it is greater than zero"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrives the value of size. """
        return self.__size

    @property
    def position(self):
        """Retrives the value of position. """
        return self.__position

    @size.setter
    def size(self, value):
        """Sets the value of size. """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) and len(value) ==
                2 and all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Returns the current square area. """
        return self.__size**2

    def my_print(self):
        """ prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            i = 0
            while i < self.__size:
                x = 0
                while x < self.__position[0]:
                    print(" ", end="")
                    x += 1

                j = 0
                while j < self.__size:
                    print("#", end="")
                    j += 1

                print()
                i += 1
