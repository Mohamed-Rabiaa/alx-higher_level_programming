#!/usr/bin/python3
from json import dumps
""" This module contains the to_json_string function """


def to_json_string(my_obj):
    """ this function returns the JSON representation of an object (string) """
    return dumps(my_obj)
