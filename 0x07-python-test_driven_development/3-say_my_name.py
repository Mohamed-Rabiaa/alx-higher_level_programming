#!/usr/bin/python3
"""This is the "3-say_my_name.py" module
the 3-say_my_name module supplies only one function, say_my_name()
which prints My name is <first name> <last name> and raises
typeError if first_name or last_name is not a string
"""

def say_my_name(first_name, last_name=""):
    """
    The function say_my_name prints My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {0} {1}".format(first_name, last_name))
