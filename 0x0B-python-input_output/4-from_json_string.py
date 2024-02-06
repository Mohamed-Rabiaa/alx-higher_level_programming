#!/usr/bin/python3
""" This module contains the from_json_string function """


from json import loads


def from_json_string(my_str):
    """ This function returns an object (Python data structure)
    represented by a JSON string """
    return loads(my_str)
