#!/usr/bin/python3
def number_keys(a_dictionary):
    if not a_dictionary:
        return 0
    keys_list = list(a_dictionary)
    keys_counter = 0
    for i in range(len(keys_list)):
        keys_counter += i
    return keys_counter
