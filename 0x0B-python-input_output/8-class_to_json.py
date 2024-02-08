#!/usr/bin/python3
""" This module contains the class_to_json function """


import json


def class_to_json(obj):
    """
    This function returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of
    an object
    """
    return obj.__dict__
