#!/usr/bin/python3
"""This is the "add_integer" module
the add_integer module supplies one function, add_integer(). which adds
two integers or floats and raises TypeError in case a or b are
not integers nor floats
"""


def add_integer(a, b=98):
    """
    The add_integer function adds two integers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    elif isinstance(b, float):
        b = int(b)

    return a + b
