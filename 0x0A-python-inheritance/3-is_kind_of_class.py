#!/usr/bin/python3
""" This module defines the is_same_class function """


def is_kind_of_class(obj, a_class):
    """ This function returns True if the object is exactly
    an instance of the specified class ; otherwise False """

    return isinstance(obj, a_class)
