#!/usr/bin/python3
""" This is the 1-my_list module """


class MyList(list):
    """ class MyList defines one function print_sorted """

    def print_sorted(self):
        """ This function prints the list, but sorted (ascending sort) """
        if not self:
            return
        print(sorted(self))
