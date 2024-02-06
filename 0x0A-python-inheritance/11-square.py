#!/usr/bin/python3
""" This module contains the Square class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This class inherits from the Rectangle class and
    overrides the area function """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Overriding the area function """
        return self.__size**2

    def __str__(self):
        """ Overriding the str function """
        return "[Square] {0}/{1}".format(self.__size, self.__size)
