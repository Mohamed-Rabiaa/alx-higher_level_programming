#!/usr/bin/python3
""" This module contains the to_json_string function """


from json import dumps


def to_json_string(my_obj):
    """ this function returns the JSON representation of an object (string) """
    return dumps(my_obj)
