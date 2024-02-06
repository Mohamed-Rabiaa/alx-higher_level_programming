#!/usr/bin/python3
""" This module contains the load_from_json_file function """


from json import loads


def load_from_json_file(filename):
    """ This function creates an Object from a “JSON file” """
    with open(filename, encoding='utf-8') as f:
        s = f.read()
        return loads(s)
