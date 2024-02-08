#!/usr/bin/python3
""" This module contains the Student class """


class Student:
    """ This is the Student class """

    def __init__(self, first_name, last_name, age):
        """
        This function instantiates first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This function retrieves a dictionary representation of a Student
        instance
        """
        if attrs is None:
            return self.__dict__

        else:
            dct = {}
            for item in attrs:
                if item in self.__dict__.keys():
                    dct[item] = self.__dict__[item]
            return dct
