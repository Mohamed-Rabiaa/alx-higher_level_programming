#!/usr/bin/python3
""" This is the 1-my_list module """


class MyList(list):
    """ class MyList defines one function print_sorted """

    def print_sorted(self):
        """ This function prints the list, but sorted (ascending sort) """
        if not self:
            return
        for i in range(len(self)):
            if not isinstance(self[i], int):
                raise TypeError("element must be an integer")
        print(sorted(self))
