#!/usr/bin/python3
""" This module contains the append_file function """


def append_write(filename="", text=""):
    """ This function appends a string at the end of a text file (UTF8)
    and returns the number of characters added """
    with open(filename, 'a', encoding='utf-8') as f:
        num = f.write(text)
        return num
