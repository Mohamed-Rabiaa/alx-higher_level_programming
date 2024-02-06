#!/usr/bin/python3
""" This module contains the save_to_json_file function """


from json import dumps


def save_to_json_file(my_obj, filename):
    """ This function writes an Object to a text file,
    using a JSON representation """
    s = dumps(my_obj)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(s)
