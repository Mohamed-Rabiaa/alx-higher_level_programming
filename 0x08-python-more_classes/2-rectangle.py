#!/usr/bin/python3
""" This module contains the Rectangle class """


class Rectangle:
    """This class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """ This function initializes the width and height
        instance attributes """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the value of the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the value of the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
