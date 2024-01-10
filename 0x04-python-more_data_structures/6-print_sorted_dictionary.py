#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_list = sorted(a_dictionary)

    for key in keys_list:
        value = a_dictionary.get(key)
        print("{0}: {1}".format(key, value))
