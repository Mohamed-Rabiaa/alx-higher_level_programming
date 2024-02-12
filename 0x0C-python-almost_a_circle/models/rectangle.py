#!/usr/bin/python3
""" This module contains the Rectangle class """


from models.base import Base
from models.validate_attr import validate_attr


class Rectangle(Base):
    """ This is the Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiates the attribute of the Rectangle
        class """
        validate_attr('width', width)
        validate_attr('height', height)
        validate_attr('x', x)
        validate_attr('y', y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Returns the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the value of the width of the rectangle """
        validate_attr('width', value)
        self.__width = value

    @property
    def height(self):
        """ Returns the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the value of the height of the rectangle """
        validate_attr('height', value)
        self.__height = value

    @property
    def x(self):
        """ Returns the x of the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets the value of x of the rectangle """
        validate_attr('x', value)
        self.__x = value

    @property
    def y(self):
        """ Returns the y of the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets the value of y of the rectangle """
        validate_attr('y', value)
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        print('\n' * self.__y, end='')
        for h in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y, self.__width,
                        self.__height))

    def update(self, *args, **kwargs):
        """ Updates the Rectangle attributes """
        attr_list = ['id', 'width', 'height', 'x', 'y']

        if args:
            for i, arg in enumerate(args):
                if i < len(attr_list):
                    setattr(self, attr_list[i], arg)
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        dct = {}
        dct['x'] = self.__dict__['_Rectangle__x']
        dct['y'] = self.__dict__['_Rectangle__y']
        dct['id'] = self.__dict__['id']
        dct['height'] = self.__dict__['_Rectangle__height']
        dct['width'] = self.__dict__['_Rectangle__width']

        return dct
