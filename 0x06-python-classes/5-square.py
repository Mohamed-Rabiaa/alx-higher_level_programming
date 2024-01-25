#!/usr/bin/python3
""" This module defines the class 'Square' """


class Square:
    """ Creating a class named 'Square' with a private
    instance attribute size. """

    def __init__(self, size=0):
        """ initializing the size attribute and checking if it is an integer
        and if it is greater than zero"""
        self.__size = size

    @property
    def size(self):
        """Retrives the value of size. """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size. """
        self.__size = value
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

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
                j = 0
                while j < self.__size:
                    print("#", end="")
                    j += 1
                print()
                i += 1
