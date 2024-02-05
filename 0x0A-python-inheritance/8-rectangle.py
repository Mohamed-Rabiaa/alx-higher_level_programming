#!/usr/bin/python3
"""" This is the 8-rectangle module """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This is the Rectangle class and it inherits from
    the 'BaseGeometry' class"""
    def __init__(self, width, height):
        """ This is the constructor of the Rectangle class
        width and height must be private and positive integers,
        validated by integer_validator """

        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height
