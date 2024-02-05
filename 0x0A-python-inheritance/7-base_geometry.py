#!/usr/bin/python3
""" This module contains the BaseGeometry class """


class BaseGeometry:
    """ The BaseGeometry class defines one function, area() """
    def area(self):
        """ This function raises an Exception with the message area()
        is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This function validates value """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise TypeError(name + " must be greater than 0")
